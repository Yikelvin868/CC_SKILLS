# HOMSH FPGA Integrator — 系统集成专家

## Overview

虹膜识别 FPGA 系统的系统集成专家。负责模块间接口对接与集成测试、AXI/AXI-Stream 总线互联、顶层约束文件生成、Vivado 工程管理、固件/驱动协同、生产测试方案，以及版本管理与发布流程。确保各子模块无缝集成为完整的虹膜识别系统。

## When to Use

- 多个 RTL 模块需要集成为完整系统
- AXI/AXI-Stream 总线互联设计
- 顶层 XDC 约束文件生成与维护
- Vivado IP Integrator / Block Design 工程管理
- FPGA 与 MCU 固件协同开发
- 生产测试方案制定
- 版本发布与配置管理

## Core Competencies

### 1. 模块间接口对接

**虹膜识别系统顶层互联架构：**
```
                    AXI-Lite (MCU 控制)
                         │
┌────────┐    ┌──────────┴──────────┐    ┌──────────┐
│ Camera │    │    Control FSM      │    │ SPI/I2C  │
│ DVP IF │    │  (寄存器映射+中断)    │    │ Slave    │
└───┬────┘    └──────────┬──────────┘    └────┬─────┘
    │ AXI-S              │                    │
    ▼                    │ ctrl signals       │ to MCU
┌────────┐    ┌──────────┐    ┌──────────┐    │
│Preproc │───→│Normalize │───→│  Gabor   │    │
│ 640×480│AXI-S│ Strip   │AXI-S│ Filter  │    │
└────────┘    └──────────┘    └────┬─────┘    │
                                   │ AXI-S    │
                              ┌────▼─────┐    │
                              │ Encoder  │    │
                              │+Matcher  │────┘
                              └──────────┘
                               match_result
```

**接口对接检查清单：**

| 接口 | 上游模块 | 下游模块 | 数据宽度 | 时钟域 | 握手协议 |
|------|---------|---------|---------|--------|---------|
| cam_axis | Camera IF | Preprocess | 8-bit | pclk→sys_clk | AXI-S + CDC FIFO |
| prep_axis | Preprocess | Normalize | 8-bit | sys_clk | AXI-S |
| norm_axis | Normalize | Gabor | 8-bit | sys_clk | AXI-S |
| gabor_axis | Gabor | Encoder | 2-bit×24 | sys_clk | AXI-S |
| code_axis | Encoder | Matcher | 2048-bit | sys_clk | AXI-S (TLAST=1/code) |
| ctrl_axi | MCU SPI | Control FSM | 32-bit | sys_clk | AXI-Lite |

**跨时钟域 FIFO 模板：**
```systemverilog
// Camera PCLK → System CLK 域转换
xpm_fifo_async #(
    .CDC_SYNC_STAGES (3),
    .FIFO_MEMORY_TYPE("block"),
    .FIFO_READ_LATENCY(0),     // First-Word-Fall-Through
    .FIFO_WRITE_DEPTH(2048),   // 至少 2 行缓冲
    .READ_DATA_WIDTH(8),
    .WRITE_DATA_WIDTH(8)
) u_cam_cdc_fifo (
    .wr_clk   (pclk),
    .wr_en    (pixel_valid),
    .din      (pixel_data),
    .full     (fifo_full),
    .rd_clk   (sys_clk),
    .rd_en    (fifo_rd_en),
    .dout     (fifo_dout),
    .empty    (fifo_empty),
    .rst      (~rst_n)
);
```

### 2. AXI/AXI-Stream 总线互联

**AXI-Stream 互联规范：**
```systemverilog
// 标准 AXI-Stream 接口定义（虹膜系统统一）
interface axis_if #(
    parameter DATA_WIDTH = 8,
    parameter USER_WIDTH = 1
);
    logic [DATA_WIDTH-1:0] tdata;
    logic                  tvalid;
    logic                  tready;
    logic                  tlast;   // 行尾/帧尾
    logic [USER_WIDTH-1:0] tuser;   // tuser[0] = SOF (帧头)

    modport master (output tdata, tvalid, tlast, tuser, input  tready);
    modport slave  (input  tdata, tvalid, tlast, tuser, output tready);
endinterface
```

**AXI-Lite 寄存器映射（MCU 控制接口）：**

| 地址偏移 | 寄存器名 | 读写 | 位域 | 说明 |
|---------|---------|------|------|------|
| 0x00 | CTRL | RW | [0] start, [1] reset, [2] mode | 系统控制 |
| 0x04 | STATUS | RO | [0] busy, [1] done, [2] error | 系统状态 |
| 0x08 | IRQ_EN | RW | [0] done_irq, [1] err_irq | 中断使能 |
| 0x0C | IRQ_STATUS | RW1C | [0] done_flag, [1] err_flag | 中断状态 |
| 0x10 | HD_THRESH | RW | [7:0] threshold | 汉明距离阈值 |
| 0x14 | HD_RESULT | RO | [7:0] distance | 匹配结果 |
| 0x18 | MATCH_ID | RO | [15:0] template_id | 匹配模板 ID |
| 0x1C | FRAME_CNT | RO | [31:0] count | 帧计数器 |
| 0x20 | ROI_X | RO | [9:0] pupil_x | 瞳孔 X 坐标 |
| 0x24 | ROI_Y | RO | [9:0] pupil_y | 瞳孔 Y 坐标 |
| 0x28 | ROI_R | RO | [7:0] pupil_r, [15:8] iris_r | 瞳孔/虹膜半径 |
| 0x2C | VERSION | RO | [31:0] git_hash | 固件版本号 |

### 3. 顶层约束文件 (XDC)

```tcl
# iris_top.xdc — 虹膜识别系统顶层约束（Artix-7 XC7A100T）

# ============================================================
# 时钟约束
# ============================================================
# 主时钟 50MHz
create_clock -period 20.000 -name sys_clk_50 [get_ports clk_50m]

# 相机像素时钟 24MHz (由 FPGA 输出，相机回环)
create_clock -period 41.667 -name cam_pclk [get_ports cam_pclk]

# 时钟域间约束
set_clock_groups -asynchronous \
    -group [get_clocks sys_clk_50] \
    -group [get_clocks cam_pclk]

# ============================================================
# 引脚分配 — Camera DVP 接口 (Bank 13, VCCO=1.8V)
# ============================================================
set_property PACKAGE_PIN U18 [get_ports cam_pclk]
set_property PACKAGE_PIN V18 [get_ports cam_vsync]
set_property PACKAGE_PIN W18 [get_ports cam_href]
set_property PACKAGE_PIN U19 [get_ports {cam_data[0]}]
set_property PACKAGE_PIN V19 [get_ports {cam_data[1]}]
set_property PACKAGE_PIN W19 [get_ports {cam_data[2]}]
set_property PACKAGE_PIN U20 [get_ports {cam_data[3]}]
set_property PACKAGE_PIN V20 [get_ports {cam_data[4]}]
set_property PACKAGE_PIN W20 [get_ports {cam_data[5]}]
set_property PACKAGE_PIN Y18 [get_ports {cam_data[6]}]
set_property PACKAGE_PIN Y19 [get_ports {cam_data[7]}]
set_property IOSTANDARD LVCMOS18 [get_ports cam_*]

# Camera I2C (SCCB)
set_property PACKAGE_PIN AA18 [get_ports cam_scl]
set_property PACKAGE_PIN AB18 [get_ports cam_sda]
set_property IOSTANDARD LVCMOS18 [get_ports cam_sc*]
set_property PULLUP true [get_ports cam_scl]
set_property PULLUP true [get_ports cam_sda]

# Camera XCLK 输出 (24MHz)
set_property PACKAGE_PIN T18 [get_ports cam_xclk]
set_property IOSTANDARD LVCMOS18 [get_ports cam_xclk]
set_property SLEW FAST [get_ports cam_xclk]

# ============================================================
# 引脚分配 — SPI Slave (MCU 通信, Bank 14, VCCO=3.3V)
# ============================================================
set_property PACKAGE_PIN J15 [get_ports spi_sck]
set_property PACKAGE_PIN K15 [get_ports spi_mosi]
set_property PACKAGE_PIN L15 [get_ports spi_miso]
set_property PACKAGE_PIN M15 [get_ports spi_cs_n]
set_property IOSTANDARD LVCMOS33 [get_ports spi_*]

# MCU 中断输出
set_property PACKAGE_PIN N15 [get_ports irq_n]
set_property IOSTANDARD LVCMOS33 [get_ports irq_n]

# ============================================================
# 引脚分配 — NIR LED 控制
# ============================================================
set_property PACKAGE_PIN P15 [get_ports led_pwm]
set_property IOSTANDARD LVCMOS33 [get_ports led_pwm]
set_property SLEW FAST [get_ports led_pwm]

# ============================================================
# 引脚分配 — 状态指示
# ============================================================
set_property PACKAGE_PIN H17 [get_ports led_done]
set_property PACKAGE_PIN J17 [get_ports led_error]
set_property PACKAGE_PIN K17 [get_ports led_match]
set_property IOSTANDARD LVCMOS33 [get_ports led_*]

# ============================================================
# QSPI Flash 配置
# ============================================================
set_property BITSTREAM.CONFIG.SPI_BUSWIDTH 4 [current_design]
set_property CONFIG_MODE SPIx4 [current_design]
set_property BITSTREAM.CONFIG.CONFIGRATE 50 [current_design]

# ============================================================
# 其他
# ============================================================
set_property BITSTREAM.GENERAL.COMPRESS TRUE [current_design]
set_property CFGBVS VCCO [current_design]
set_property CONFIG_VOLTAGE 3.3 [current_design]
```

### 4. Vivado 工程管理

**工程目录结构：**
```
iris_fpga/
├── rtl/                    # RTL 源文件
│   ├── iris_top.sv
│   ├── camera_if.sv
│   ├── iris_preprocess.sv
│   ├── iris_normalize.sv
│   ├── iris_gabor_filter.sv
│   ├── iris_encoder.sv
│   ├── iris_matcher.sv
│   ├── ctrl_fsm.sv
│   ├── spi_slave.sv
│   └── common/
│       ├── axis_fifo.sv
│       ├── cdc_sync.sv
│       └── axi_lite_regs.sv
├── tb/                     # Testbench
│   ├── tb_iris_top.sv
│   └── tb_*.sv
├── xdc/                    # 约束文件
│   ├── iris_top.xdc
│   ├── iris_timing.xdc
│   └── iris_debug.xdc
├── ip/                     # Vivado IP
│   ├── clk_wiz_0/
│   └── xpm_fifo/
├── hls/                    # HLS IP
│   └── gabor_hls/
├── scripts/                # Tcl 脚本
│   ├── build.tcl           # 非工程模式一键构建
│   ├── program.tcl         # 下载 bitstream
│   └── ila_insert.tcl      # 调试探针
├── sim/                    # 仿真输出
├── docs/                   # 设计文档
└── release/                # 发布产物
    ├── v1.0.0/
    │   ├── iris_top.bit
    │   ├── iris_top.ltx
    │   ├── iris_top.mcs
    │   └── release_notes.md
    └── v1.1.0/
```

**非工程模式构建脚本 (build.tcl)：**
```tcl
# build.tcl — Vivado 非工程模式一键构建
set PART xc7a100tftg256-1
set TOP iris_top
set OUT_DIR ./output

# 读入源文件
read_verilog -sv [glob rtl/*.sv rtl/common/*.sv]
read_xdc [glob xdc/*.xdc]
read_ip [glob ip/*/*.xci]

# 综合
synth_design -top $TOP -part $PART \
    -flatten_hierarchy rebuilt \
    -retiming on
report_utilization -file $OUT_DIR/post_synth_util.rpt
report_timing_summary -file $OUT_DIR/post_synth_timing.rpt

# 布局布线
opt_design
place_design
phys_opt_design
route_design
report_utilization -file $OUT_DIR/post_impl_util.rpt
report_timing_summary -file $OUT_DIR/post_impl_timing.rpt
report_power -file $OUT_DIR/post_impl_power.rpt

# 生成 bitstream
write_bitstream -force $OUT_DIR/${TOP}.bit
write_cfgmem -format mcs -interface SPIx4 -size 128 \
    -loadbit "up 0x0 $OUT_DIR/${TOP}.bit" \
    -file $OUT_DIR/${TOP}.mcs -force

# 生成调试探针文件
write_debug_probes -force $OUT_DIR/${TOP}.ltx

puts "Build complete: $OUT_DIR/${TOP}.bit"
```

### 5. 固件/驱动协同

**MCU 端 SPI 驱动框架（C 语言）：**
```c
// iris_fpga_drv.h — MCU 端 FPGA 驱动接口
#ifndef IRIS_FPGA_DRV_H
#define IRIS_FPGA_DRV_H

#include <stdint.h>

// 寄存器地址（与 FPGA AXI-Lite 映射一致）
#define IRIS_REG_CTRL       0x00
#define IRIS_REG_STATUS     0x04
#define IRIS_REG_IRQ_EN     0x08
#define IRIS_REG_IRQ_STATUS 0x0C
#define IRIS_REG_HD_THRESH  0x10
#define IRIS_REG_HD_RESULT  0x14
#define IRIS_REG_MATCH_ID   0x18
#define IRIS_REG_VERSION    0x2C

// 控制位
#define CTRL_START  (1 << 0)
#define CTRL_RESET  (1 << 1)

// 状态位
#define STATUS_BUSY (1 << 0)
#define STATUS_DONE (1 << 1)
#define STATUS_ERR  (1 << 2)

// API
void     iris_init(void);
void     iris_set_threshold(uint8_t threshold);
int      iris_start_capture(void);
int      iris_wait_done(uint32_t timeout_ms);
uint8_t  iris_get_hd(void);
uint16_t iris_get_match_id(void);
uint32_t iris_get_version(void);

#endif
```

**SPI 通信协议：**
```
帧格式（MCU → FPGA）：
Byte 0: [7] R/W# (0=Write, 1=Read)
         [6:0] 寄存器地址 (7-bit, 最多 128 个寄存器)
Byte 1-4: 数据 (32-bit, MSB first)

写操作：MCU 发送 5 字节，FPGA 无响应
读操作：MCU 发送 1 字节地址，FPGA 返回 4 字节数据

SPI 参数：
- Mode: CPOL=0, CPHA=0 (Mode 0)
- Clock: ≤ 25MHz (FPGA sys_clk/4)
- CS: Active Low
- Bit Order: MSB First
```

### 6. 生产测试方案

**BIST (Built-In Self-Test) 设计：**
```systemverilog
// 内建自测试模块
module iris_bist (
    input  logic clk, rst_n,
    input  logic bist_enable,
    output logic bist_pass,
    output logic bist_done,
    output logic [7:0] bist_error_code
);
    // 测试项目
    typedef enum logic [3:0] {
        BIST_IDLE,
        BIST_BRAM_TEST,    // BRAM 读写测试（棋盘格模式）
        BIST_DSP_TEST,     // DSP48 乘法验证
        BIST_LOOPBACK,     // 数据通路环回测试
        BIST_CLK_CHECK,    // 时钟频率校验
        BIST_CAMERA_CHECK, // 相机通信测试（I2C 读 ID）
        BIST_DONE
    } bist_state_t;
    // ...
endmodule
```

**生产测试流程：**

| 测试项 | 方法 | 通过条件 | 耗时 |
|--------|------|---------|------|
| JTAG 连接 | Vivado hw_manager | IDCODE 正确 | 2s |
| 配置下载 | .bit 文件下载 | DONE 拉高 | 5s |
| BIST 全套 | VIO 触发自测试 | bist_pass=1 | 10s |
| 相机通信 | I2C 读传感器 ID | 返回 OV7251 ID | 1s |
| 图像采集 | 采集 1 帧检查 | 非全黑/全白 | 2s |
| SPI 通信 | MCU 读 VERSION 寄存器 | 版本号正确 | 1s |
| 虹膜识别 | 标准测试图像 | HD < 0.33 | 5s |
| **总计** | | | **~26s** |

### 7. 版本管理与发布流程

**版本号规则：**
```
v{MAJOR}.{MINOR}.{PATCH}[-{LABEL}]

MAJOR: 架构变更（接口不兼容）
MINOR: 功能新增（向下兼容）
PATCH: Bug 修复

Label: alpha, beta, rc1

示例：
v1.0.0       — 首个生产版本
v1.1.0       — 增加旋转补偿功能
v1.1.1       — 修复 Gabor 系数加载 Bug
v2.0.0-alpha — 新架构（CNN 替代 Gabor）
```

**发布检查清单：**
```
□ 综合/实现无错误、无关键警告
□ 时序约束全部满足（WNS > 0）
□ 资源使用率 < 80%
□ 全部回归测试通过
□ 覆盖率 ≥ 90%
□ 功耗报告在预算内
□ BIST 测试通过
□ 板级验证通过（至少 3 块板）
□ .bit + .ltx + .mcs 文件归档
□ Release Notes 编写完成
□ Git Tag 创建
```

**版本信息嵌入 RTL：**
```systemverilog
// 版本信息自动从 git 注入
`ifndef GIT_HASH
`define GIT_HASH 32'hDEAD_BEEF
`endif

module version_reg (
    input  logic        clk,
    input  logic [6:0]  addr,
    output logic [31:0] rdata
);
    localparam VERSION_MAJOR = 8'd1;
    localparam VERSION_MINOR = 8'd1;
    localparam VERSION_PATCH = 8'd0;

    always_comb begin
        case (addr)
            7'h2C: rdata = {VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH, 8'h00};
            7'h30: rdata = `GIT_HASH;
            default: rdata = 32'h0;
        endcase
    end
endmodule
```

## Deliverables

- 顶层 RTL (iris_top.sv) 含模块互联
- XDC 约束文件（引脚 + 时序 + 配置）
- Vivado 工程（或非工程模式 build.tcl）
- AXI-Lite 寄存器映射文档
- MCU 驱动源码（C 头文件 + 实现）
- SPI 通信协议文档
- BIST 测试模块 RTL
- 生产测试规程
- 版本发布包（.bit + .ltx + .mcs + Release Notes）

## Related Agents

- ← `homsh-fpga-rtl-coder`: 接收各子模块 RTL
- ← `homsh-fpga-hls-converter`: 接收 HLS 生成的 IP
- ← `homsh-fpga-hw-designer`: 接收硬件引脚约束
- → `homsh-fpga-verifier`: 交付顶层集成进行系统级验证
- → `homsh-fpga-debugger`: 板级集成测试中的问题调试
- ↔ `homsh-fpga-architect`: 架构调整时的接口变更协同

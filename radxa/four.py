# -*- coding: utf-8 -*-
# Written by Hugh Sheehy @hughsheehy

"""
Alternative pin mappings for Radxa Rock 4 B (should apply to all Rock 4s...pin mappings are the same)
(see https://wiki.radxa.com/Rockpi4/hardware/gpio)
Usage:
.. code:: python
   import radxa.four
   from OPi import GPIO
   GPIO.setmode(radxa.four.BOARD) or GPIO.setmode(radxa.zero.BCM)
"""


# Radxa 4 series physical board pin to GPIO pin
BOARD = {
    3:      71,    # GPIO2_A7  | I2C7_SDA
    5:      72,    # GPIO2_B0  | I2C7_SCL
    7:      75,    # GPIO2_B3  | SPI2_CLK 
    11:     146,   # GPIO4_C2  | PWM0 
    13:     150,   # GPIO4_C6  | PWM1 
    19:     40,    # GPIO1_B0   | UART4_TXD | SPI1_TXD
    21:     39,    # GPIO1_A7   | UART4_RXD | SPI1_RXD
    23:     41,    # GPIO1_B1   | SPI1_CLK 
    27:     64,    # GPIO2_A0   | I2C2_SDA | 
    29:     74,    # GPIO2_B2   | SPI2_TXD | SPI2_TXD
    31:     73,    # GPIO2_B1   | SPI2_RXD  | I2C6_SDA
    33:     76,     # GPIO2_B4   | SPI2_CSn
    35:     133,   # GPIO4_A5   | I2S1_LRCK_TX
    37:     158,   # GPIO4_D6
    8:      148,    # GPIO4_C4  | UART2_TXD
    10:     147,    # GPIO4_C3  | UART2_RXD
    12:     131,    # GPIO4_A3  | I2S1_SCLK	
    16:     154,    # GPIO4_D2 
    18:     156,    # GPIO4_D4 
    22:     157,    # GPIO4_D5
    24:     42,    # GPIO1_B2   |SPI1_CSn 
    28:     65,    # GPIO2_A1  | I2C2_CLK 
    32:     112,    # GPIO3_C0	| SPDIF_TX	| UART3_CTSn
    36:     132,    # GPIO4_A4	| I2S1_LRCK_RX
    38:     134,    # GPIO4_A6	| I2S1_SDI
    40:     135,    # GPIO4_A7	|I2S1_SDO
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
###############################################################################
#Details of the frequncies available for LoRaWAN usage
#Copyright (C) 2018 Philip Basford

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as
#published by the Free Software Foundation, either version 3 of the
#License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.

#You should have received a copy of the GNU Affero General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.
###############################################################################

#https://www.thethingsnetwork.org/wiki/LoRaWAN/Frequencies/Frequency-Plans

#AU915-928

START_CH = 8
END_CH = 15

# DR0, ..., DR13
DR = ([12,7], [11,7], [10,7], [9,7],[8,7],[7,7],[8,9],[0,0],[12,9], [11,9], [10,9], [9,9],[8,9],[7,9])

CHANNELS = tuple([i for i in range(START_CH, END_CH)])
CHANNELS_HIGH = tuple([i for i in range(64,71)])

LORA_FREQS = tuple([(i*2+9152)/10 for i in range(START_CH, END_CH)])
LORA_FREQS_HIGH = tuple([((i%8)*5+9159)/10 for i in range(64,71)])

LORA_FREQS_DOWNLINK =  tuple([(i*6+9233)/10 for i in range(0, 7)])




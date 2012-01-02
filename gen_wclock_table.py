# Dictionary of all LED strings and their 32-bit position
LED_Bit_Dictionary = {
	"IT IS":	8,
	"A QUA":	9,
	"RTER":		10,
	"TENm":		11,
	"TWEm":		12,
	"NTY":		13,
	"FIVEm":	14,
	"MINU":		0,
	"TES":		1,
	"HALF":		2,
	"PAST":		3,
	"TO":		4,
	"ONE":		5,
	"TWO":		6,
	"THR":		7,
	"EE":		24,
	"FOUR":		26,
	"FIVE":		25,
	"SIX":		27,
	"SEV":		28,
	"EN":		29,
	"EIG":		30,
	"HT":		31,
	"NINE":		16,
	"TEN":		17,
	"ELE":		18,
	"VEN":		19,
	"TWE":		20,
	"LVE":		21,
	"OCL":		22,
	"OCK":		23,
}

# LED Strings "IT IS", "O'CL", "OCK" are always on
LED_Template = ["IT IS", "OCL", "OCK"]

# LED Strings for hours "ONE" ... "TWELVE"
LED_Hours = [
	["ONE"],		# 1	- "ONE"
	["TWO"],		# 2	- "TWO"
	["THR", "EE"],		# 3	- "THREE"
	["FOUR"],		# 4 	- "FOUR"
	["FIVE"],		# 5 	- "FIVE"
	["SIX"],		# 6	- "SIX"
	["SEV", "EN"],		# 7	- "SEVEN"
	["EIG", "HT"],		# 8	- "EIGHT"
	["NINE"],		# 9	- "NINE"
	["TEN"],		# 10	- "TEN"
	["ELE", "VEN"],		# 11	- "ELEVEN"
	["TWE", "LVE"],		# 12	- "TWELVE"
]

# LED Strings for five minute intervals
LED_Minutes = [
	#(words, hour inc)
	([], 						0), # 00
	(["FIVEm", "MINU", "TES", "PAST"],		0), # 05 - "FIVE" "PAST"
	(["TENm", "MINU", "TES", "PAST"],		0), # 10 - "TEN" "PAST"
	(["A QUA", "RTER", "PAST"], 			0), # 15 - "A QUARTER" "PAST"
	(["TWEm", "NTY", "MINU", "TES", "PAST"],	0), # 20 - "TWENTY" "PAST"
	(["TWEm", "NTY", "FIVEm", "MINU", "TES", "PAST"],0), # 25 - "TWENTY" "FIVE" "PAST"
	(["HALF", "PAST"],				0), # 30 - "HALF" "PAST"
	(["TWEm", "NTY", "FIVEm", "MINU", "TES", "TO"],	1), # 35 - "TWENTY" "FIVE" "TO"
	(["TWEm", "NTY", "MINU", "TES", "TO"],		1), # 40 - "TWENTY"  "TO"
	(["A QUA", "RTER", "TO"], 			1), # 45 - "A QUARTER" "TO"
	(["TENm", "MINU", "TES", "TO"],			1), # 50 - "TEN" "TO"
	(["FIVEm", "MINU", "TES", "TO"],		1), # 55 - "FIVE" "TO"
]

def led_bit_lookup(words):
	bits = 0
	for w in words:
		bits = bits | (1 << LED_Bit_Dictionary[w])
	return bits

print "led_time_table:"

for hours in range(12):
	for minutes in range(60/5):
		(led_min_words, inc) = LED_Minutes[minutes]
		led_hour_words = LED_Hours[(hours+inc) % 12]

		led_bits = led_bit_lookup(LED_Template) | led_bit_lookup(led_min_words) | led_bit_lookup(led_hour_words)

		led_bits_high = (led_bits & 0xFFFF0000) >> 16
		led_bits_low = (led_bits & 0xFFFF)
		offset = (hours*12) + minutes

		print "\t.word 0x%04X, 0x%04X\t; %02d:%02d:00  Offset: %d" % (led_bits_high, led_bits_low, hours+1, minutes*5, offset << 2)


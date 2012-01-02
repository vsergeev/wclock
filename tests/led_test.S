; Test for the LED shift registers

demoloop:
	ldi R16, 0xff
	ldi R17, 0xff
	ldi R18, 0x00

	ldi R19, 0x00
	rcall led_update
	rcall delay
	ldi R19, 0x01
	rcall led_update
	rcall delay
	ldi R19, 0x02
	rcall led_update
	rcall delay
	ldi R19, 0x08
	rcall led_update
	rcall delay
	ldi R19, 0x10
	rcall led_update
	rcall delay
	ldi R19, 0x20
	rcall led_update
	rcall delay
	ldi R19, 0x40
	rcall led_update
	rcall delay
	ldi R19, 0x80
	rcall led_update
	rcall delay

	ldi R19, 0x00

	ldi R18, 0x00
	rcall led_update
	rcall delay
	ldi R18, 0x01
	rcall led_update
	rcall delay
	ldi R18, 0x02
	rcall led_update
	rcall delay
	ldi R18, 0x08
	rcall led_update
	rcall delay
	ldi R18, 0x10
	rcall led_update
	rcall delay
	ldi R18, 0x20
	rcall led_update
	rcall delay
	ldi R18, 0x40
	rcall led_update
	rcall delay
	ldi R18, 0x80
	rcall led_update
	rcall delay

	ldi R18, 0xFF
	ldi R19, 0xFF
	rcall led_update
	rcall delay
	ldi R18, 0x00
	ldi R19, 0x00
	rcall led_update
	rcall delay
	ldi R18, 0xFF
	ldi R19, 0xFF
	rcall led_update
	rcall delay
	ldi R18, 0x00
	ldi R19, 0x00
	rcall led_update
	rcall delay
	ldi R18, 0xFF
	ldi R19, 0xFF
	rcall led_update
	rcall delay
	ldi R18, 0x00
	ldi R19, 0x00
	rcall led_update
	rcall delay

	ldi R18, 0xFF
	ldi R19, 0xFF
	rcall led_update
	rcall delay
	rcall delay
	rcall delay
	rcall delay
	rcall delay
	rcall delay
	rcall delay
	rcall delay
	rcall delay
	rcall delay
	rcall delay

	rjmp demoloop

longdelay:
	rcall delay
	rcall delay
	rcall delay
	rcall delay
	rcall delay
	rcall delay
	rcall delay
	rcall delay
	rcall delay
	rcall delay
	ret

delay:
	ldi r20, 0xff

	.loop0:
		ldi r21, 0x7f
		.loop1:
			dec r21
			brne .loop1
		dec r20
		brne .loop0

	ret



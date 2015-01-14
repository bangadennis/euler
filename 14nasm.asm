mov ecx, 1000000 ; init loop counter
		xor edi, edi ; highest starting number found
		xor esi, esi ; length of above chain
outer:
		dec ecx ; try next number
		jz _done ; if number is zero, stop

		mov ebx, ecx ; copy current number to ebx
		xor eax, eax ; current chain length counter
	inner:
		cmp esi, eax ; is this the longest chain?
		cmovc edi, ecx ; if so update...
		cmovc esi, eax ; ... the max variables
		cmp ebx, 1 ; loop if chain is at 1 (end)
		jz outer

		test ebx, 1 ; odd number?
		jnz _odd    ; yes, jump
		shr ebx, 1 ; no, divide by 2, 
		inc eax ; and increase chain length counter
		jmp inner ; loop
		_odd:
			lea ebx, [ebx*2+ebx+1] ; 3n+1
			inc eax ; increase chain length counter
			jmp inner ; loop
		jmp outer
_done:
		mov answer, edi
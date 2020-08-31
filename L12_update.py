#!/usr/bin/python

	new_hand = self.hand.copy()
		for letter in word:
			try:
				new_hand[letter] -= 1
			except KeyError:
				# if 'letter' isn't in the hand, we can't make the word from this hand.
				return False
		for letter in new_hand.keys():
			# If any of the letter counts of the new hand are less than zero after the
			# update, then we can't make the word from this hand.
			if new_hand[letter] < 0:
				return False
		# If we've gotten to here, we must be able to make the word from this hand.
		# Set self.hand to the new, updated hand and return True.
		self.hand = new_hand
		return True
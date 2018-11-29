import Model
import re


def ControllerButton(whichtable, searchText):
	print("Passando pela controller")
	return Model.Select(whichtable, searchText)

def CheckField(string):
	cpfPattern = r"(?:^\d{3}.\d{3}.\d{3}-\d{2}$)"
	# phonePattern = r"(?:\(\d{2}\)\d{5}-\d{4}$)"
	matches = re.search(cpfPattern, string, re.IGNORECASE)
	if matches:
		print("Match: " + matches.group(0))
		return 0
	else:
		print("No match")
		return -1  



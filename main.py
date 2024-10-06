def main():
	report( "books/frankenstein.txt" )


def read_file( filename: str ):
	with open( filename ) as f:
		file_contents = f.read()
	return file_contents


def count_words( contents: str ):
	words = contents.split()
	return len( words )


def count_characters( contents: str ):
	characters = {}
	for c in contents:
		if c.isalpha():
			c2 = c.lower()
			if not c2 in characters:
				characters[ c2 ] = 0
			characters[ c2 ] += 1
	return characters


def get_sorted_characters( characters ):
	arr = []
	for c in characters:
		arr.append( ( c, characters[ c ] ) )
	return sorted( arr, key = lambda x: x[ 1 ], reverse = True )


def report( filename ):
	file_contents = read_file( filename )
	word_count = count_words( file_contents )
	characters = count_characters( file_contents )
	sorted_characters = get_sorted_characters( characters )
	print( f"--- Begin report of {filename} ---" )
	print( f"{word_count} words found in the document" )
	print( "" )
	for t in sorted_characters:
		print( f"The '{t[0]}' character was found {t[1]} times" )



main()
def calculate_triangle_nums(n: int) -> list:
    nums = set()
    for i in range(1, n+1):
        nums.add( int((0.5*i) * (i+1)) )

    return nums

if __name__ == '__main__':
    tri_nums = calculate_triangle_nums(100)
    # print(tri_nums)

    words = []
    with open('input/0042_words.txt', 'r') as infile:
        for line in infile:
            words = words + line.replace('"', '').split(',')

    # print(words[0:10])

    tri_ct = 0
    for word in words:
        val = 0
        for letter in word:
            val += ord(letter) - 64

        if val in tri_nums:
            tri_ct += 1

    print(tri_ct)
    
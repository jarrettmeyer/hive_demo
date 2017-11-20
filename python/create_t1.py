import random
import sys

# Ensure that a max lines argument was given.
if len(sys.argv) < 2:
    print "Usage python create_t1.py <max_lines>"
    exit(-1)

line = 0
max_lines = int(sys.argv[1])
path_to_file = "../demo_files/t1.txt"
path_to_lorum = "../demo_files/lorum_ipsum.txt"
percent = max_lines / 100

file_ptr = open(path_to_file, "w")
lorum_ptr = open(path_to_lorum, "r")

lorum_text = lorum_ptr.read()
lorum_text = lorum_text.replace(",", "").replace(".", "").replace("\r", "").replace("\n", "").lower()
lorum_words = lorum_text.split(" ")
lorum_ptr.close()

print "Creating %d lines..." % (max_lines)

while line < max_lines:
    line = line + 1
    word_count = random.randint(5, 50)
    words = []
    while len(words) < word_count:
        rand_index = random.randint(1, len(lorum_words)) - 1
        words.append(lorum_words[rand_index])
    file_ptr.write("%d,%s\n" % (line, " ".join(words)))
    if line % percent == 0:
        percent_done = (float(line) / float(max_lines)) * 100
        print "%.0f%% completed" % percent_done

file_ptr.close()

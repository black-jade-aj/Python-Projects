There is a major bug in line 4 that will crash your code:

* **`AttributeError: 'list' object has no attribute 'split'` (Line 4):** `fh.readlines()` returns a **list of strings** containing every line in the file, not a single string. You cannot call `.split()` on a list.
* **Missing Loop:** If your file has multiple lines, you need to loop over `fh` or `fh.readlines()`. If it only has one line, you should use `fh.readline()` or `data[0].split(",")`.
* **File Resource Leak:** The file handle `fh` is opened, but never closed using `fh.close()`. Using a `with open(...)` block is cleaner and safer.

---

### Fixed Code (For a single line of data)

If `colldata.txt` contains just **one** line of text:

```python
colldata = {}  # empty dictionary

with open("colldata.txt", "r") as fh:
    line = fh.readline().strip()  # read the single line and strip newline characters
    presdata = line.split(",")   # split on commas into a list

colldata['lastname'] = presdata[0]
colldata['firstname'] = presdata[1]
colldata['height'] = presdata[2]
colldata['weight'] = presdata[3]

print(colldata)

```

---

### Alternative (For multiple lines of data)

If your file has **multiple rows** of people and you want a list of dictionaries:

```python
all_people = []

with open("colldata.txt", "r") as fh:
    for line in fh:
        presdata = line.strip().split(",")
        if len(presdata) >= 4:
            person = {
                'lastname': presdata[0],
                'firstname': presdata[1],
                'height': presdata[2],
                'weight': presdata[3]
            }
            all_people.append(person)

```
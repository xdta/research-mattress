import re
from docx import Document
from tqdm import tqdm
import time

# Define the keyword to search for
keyword = "radio"

# Paths
doc_path = 'diary-study-entries-only.docx'
output_path = f'filtered_entries_{keyword}.txt'

# Start timing
global_start = time.time()

# 📖 Load Document
print("📖 Loading the document...")
load_start = time.time()
document = Document(doc_path)
load_end = time.time()
print(f"✅ Document loaded in {load_end - load_start:.2f} seconds.\n")

# 🔍 Extract and Split Entries by Separator
print("🔍 Splitting entries by separator...")
split_start = time.time()

# Join all paragraphs into a single text block
content = '\n'.join([para.text for para in document.paragraphs])

# Split entries by separator
entries = re.split(r'={20,}', content)  # Match 20 or more '=' characters
split_end = time.time()
print(f"✅ Split into {len(entries)} entries in {split_end - split_start:.2f} seconds.\n")

# 🛠️ Debug: Display Sample Entries
print("\n🛠️ Sample Entries for Debugging:")
for i, entry in enumerate(entries[:3]):
    print(f"\n--- Entry {i+1} ---")
    print(entry[:500])  # Print first 500 characters of each sample entry

# 🔍 Search for Keyword in Each Entry
print("\n🔍 Searching for the keyword in entries...")
filter_start = time.time()
filtered_entries = []

for i, entry in tqdm(enumerate(entries), total=len(entries), desc="Processing Entries"):
    if re.search(r'\bradio\b', entry, re.IGNORECASE):
        filtered_entries.append(entry)
filter_end = time.time()
print(f"✅ Found {len(filtered_entries)} matching entries in {filter_end - filter_start:.2f} seconds.\n")

# 💾 Save Results
save_start = time.time()
print("💾 Saving filtered entries...")
with open(output_path, 'w') as file:
    for entry in filtered_entries:
        file.write(entry + '\n\n')
save_end = time.time()
print(f"✅ Results saved in {save_end - save_start:.2f} seconds.\n")

# ⏱️ Total Runtime
global_end = time.time()
print(f"✅ Filtered entries saved to {output_path}")
print(f"🔍 {len(filtered_entries)} entries containing the keyword '{keyword}' were found.")
print(f"⏱️ Total Runtime: {global_end - global_start:.2f} seconds")

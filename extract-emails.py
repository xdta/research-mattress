

import re

def extract_emails_from_text(text):
    """
    Extract emails enclosed in < > from the provided text.
    
    Args:
        text (str): The input string containing emails.
    
    Returns:
        list: A list of extracted email addresses.
    """
    email_pattern = r'<([^<>]+@[^<>]+)>'
    return re.findall(email_pattern, text)

# Example usage
if __name__ == "__main__":
    # Input text
    input_text = "Alice Tang <xiaodita@andrew.cmu.edu>, Nikolas Martelaro <nmartela@andrew.cmu.edu>, Aditi Narasimhan <aditin@andrew.cmu.edu>, Adrian Cantu Garza <acantu2@andrew.cmu.edu>, Adwoa Asare <aasare@andrew.cmu.edu>, Alice Tang <actang2@andrew.cmu.edu>, Alyssa Ogle <aogle@andrew.cmu.edu>, Ariel Wu <yenjungw@andrew.cmu.edu>, Ashley Sanchez <ashleysa@andrew.cmu.edu>, Brenna Lindblad <blindbla@andrew.cmu.edu>, Chenyue Shen <chenyues@andrew.cmu.edu>, Ching Han Chou <chingha2@andrew.cmu.edu>, Darol Devi Njami Tchouke <dnjamitc@andrew.cmu.edu>, Ember Shan <embershs@andrew.cmu.edu>, Enze Yuan <enzey@andrew.cmu.edu>, Eric Tang <ehtang@andrew.cmu.edu>, Fiona Fisher <frf@andrew.cmu.edu>, George Pan <fuchengp@andrew.cmu.edu>, Grace Liu <gmliu@andrew.cmu.edu>, Ifeanyi Ene <iie@andrew.cmu.edu>, Isabella Shi <yaorans@andrew.cmu.edu>, Jennifer Wang <hanyiwan@andrew.cmu.edu>, Josh Rong <dingchar@andrew.cmu.edu>, Leyi Han <leyih@andrew.cmu.edu>, Mason Stark <mstark@andrew.cmu.edu>, Meihui Liu <meihuil@andrew.cmu.edu>, Mingyang Zhu <mz3@andrew.cmu.edu>, Nadia Palar <npalar@andrew.cmu.edu>, Naimah Jangha <njangha@andrew.cmu.edu>, Nicholas Ward <npward@andrew.cmu.edu>, Ray Xia <rayx@andrew.cmu.edu>, Rina Kim <rinak@andrew.cmu.edu>, Rory Cai <rorycai@andrew.cmu.edu>, Shao Ju Wang <shaojuw@andrew.cmu.edu>, Sid Kunisetty <skuniset@andrew.cmu.edu>, Storm Wright <stormw@andrew.cmu.edu>, Sunny Liu <sunnyliu@andrew.cmu.edu>, Tassy Chen <tassyc@andrew.cmu.edu>, Tianyi He <tianyihe@andrew.cmu.edu>, Wei Liu <weiliu2@andrew.cmu.edu>, Wen Hui Leng <wleng@andrew.cmu.edu>, Yiyun Wei <yiyunwei@andrew.cmu.edu>, Yuchen Dai <yuchenda@andrew.cmu.edu>, Zoe So <zxs@andrew.cmu.edu>"
    
    # Extract emails
    emails = extract_emails_from_text(input_text)
    
    # Print results
    print("Extracted Emails:")
    for email in emails:
        print(email)

def duplicate_count(text):
    text = text.lower()
    return len(set([i for i in text if text.count(i) > 1]))


print(duplicate_count('WVb2j2wgctQnwXoksdK0hFKS2NfQTQUTfzzLLuH4Ib0L4CDi4N1gavsvfLENR8v'))  # 20
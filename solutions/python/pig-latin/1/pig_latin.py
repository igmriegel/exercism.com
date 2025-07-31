def translate(text: str) -> str:
    no_case_str = text.casefold()
    vowel_sounds = ("a", "e", "i", "o", "u", "xr", "yt")

    if " " in no_case_str:
        return " ".join([translate(word) for word in no_case_str.split(" ")])
    
    if no_case_str.startswith(vowel_sounds):
        return text + "ay"

    if not no_case_str.startswith(vowel_sounds):
        if no_case_str.startswith(("squ", "thr", "sch", "thr")):
            return text[3:] + text[0:3] + "ay"

        if no_case_str.startswith(("ch", "st", "qu", "th", "rh")):
            return text[2:] + text[0:2] + "ay"

        if len(no_case_str) == 2 and no_case_str[-1] == "y":
            return text[1] + text[0] + "ay"
        
        return text[1:] + text[0] + "ay"

pub fn is_leap_year(year: u64) -> bool {
    let mod_4 = year % 4 == 0;
    let mod_100 = year % 100 == 0;
    let mod_400 = year % 400 == 0;

    if mod_100 & !mod_400 {
        false
    } else if mod_4 | (mod_4 & mod_400) {
        true
    } else {
        false
    }
}

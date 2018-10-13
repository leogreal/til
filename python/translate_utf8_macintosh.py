def translate_macintosh_utf8(value):
    # macintosh / utf-8
    # http://string-functions.com/encodingtable.aspx?encoding=65001&decoding=10000
    return value\
        .replace('¬Ä', '').replace('¬Å', '').replace('¬Ç', '').replace('¬É', '').replace('¬Ñ', '')\
        .replace('¬Ö', '').replace('¬Ü', '').replace('¬á', '').replace('¬à', '').replace('¬â', '')\
        .replace('¬ä', '').replace('¬ã', '').replace('¬å', '').replace('¬ç', '').replace('¬é', '')\
        .replace('¬è', '').replace('¬ê', '').replace('¬ë', '').replace('¬í', '').replace('¬ì', '')\
        .replace('¬î', '').replace('¬ï', '').replace('¬ñ', '').replace('¬ó', '').replace('¬ò', '')\
        .replace('¬ô', '').replace('¬ö', '').replace('¬õ', '').replace('¬ú', '').replace('¬ù', '')\
        .replace('¬û', '').replace('¬ü', '').replace('¬†', ' ').replace('¬°', '¡').replace('¬¢', '¢')\
        .replace('¬£', '£').replace('¬§', '¤').replace('¬•', '¥').replace('¬¶', '¦').replace('¬ß', '§')\
        .replace('¬®', '¨').replace('¬©', '©').replace('¬™', 'ª').replace('¬´', '«').replace('¬¨', '¬')\
        .replace('¬≠', '').replace('¬Æ', '®').replace('¬Ø', '¯').replace('¬∞', '°').replace('¬±', '±')\
        .replace('¬≤', '²').replace('¬≥', '³').replace('¬¥', '´').replace('¬µ', 'µ').replace('¬∂', '¶')\
        .replace('¬∑', '·').replace('¬∏', '¸').replace('¬π', '¹').replace('¬∫', 'º').replace('¬ª', '»')\
        .replace('¬º', '¼').replace('¬Ω', '½').replace('¬æ', '¾').replace('¬ø', '¿').replace('√Ä', 'À')\
        .replace('√Å', 'Á').replace('√Ç', 'Â').replace('√É', 'Ã').replace('√Ñ', 'Ä').replace('√Ö', 'Å')\
        .replace('√Ü', 'Æ').replace('√á', 'Ç').replace('√à', 'È').replace('√â', 'É').replace('√ä', 'Ê')\
        .replace('√ã', 'Ë').replace('√å', 'Ì').replace('√ç', 'Í').replace('√é', 'Î').replace('√è', 'Ï')\
        .replace('√ê', 'Ð').replace('√ë', 'Ñ').replace('√í', 'Ò').replace('√ì', 'Ó').replace('√î', 'Ô')\
        .replace('√ï', 'Õ').replace('√ñ', 'Ö').replace('√ó', '×').replace('√ò', 'Ø').replace('√ô', 'Ù')\
        .replace('√ö', 'Ú').replace('√õ', 'Û').replace('√ú', 'Ü').replace('√ù', 'Ý').replace('√û', 'Þ')\
        .replace('√ü', 'ß').replace('√†', 'à').replace('√°', 'á').replace('√¢', 'â').replace('√£', 'ã')\
        .replace('√§', 'ä').replace('√•', 'å').replace('√¶', 'æ').replace('√ß', 'ç').replace('√®', 'è')\
        .replace('√©', 'é').replace('√™', 'ê').replace('√´', 'ë').replace('√¨', 'ì').replace('√≠', 'í')\
        .replace('√Æ', 'î').replace('√Ø', 'ï').replace('√∞', 'ð').replace('√±', 'ñ').replace('√≤', 'ò')\
        .replace('√≥', 'ó').replace('√¥', 'ô').replace('√µ', 'õ').replace('√∂', 'ö').replace('√∑', '÷')\
        .replace('√∏', 'ø').replace('√π', 'ù').replace('√∫', 'ú').replace('√ª', 'û').replace('√º', 'ü')\
        .replace('√Ω', 'ý').replace('√æ', 'þ').replace('√ø', 'ÿ')

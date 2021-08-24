function Previous()
{
	if (thing > 0)
	{
		thing = thing - 1;
		document.getElementById("thing").innerHTML = things[thing];
	}
	else
	{
		thing = things.length - 1;
		document.getElementById("thing").innerHTML = things[thing];
	}
}
function Next()
{
	if (thing < things.length - 1)
	{
		thing = thing + 1;
		document.getElementById("thing").innerHTML = things[thing];
	}
	else
	{
		thing = 0;
		document.getElementById("thing").innerHTML = things[thing];
	}
}
function Back()
{
	if ((place > 0) && (place != -1))
	{
	    if (solved[place - 1] != -1)
	    {
	        place -= 1;
            SetAppearance();
		}
	}
}
function Forward()
{
	if ((place < places.length - 1) && (place != -1))
	{
		if (solved[place + 1] != -1)
	    {
	        place += 1;
            SetAppearance();
		}
	}
}
function SetAppearance()
{
    document.getElementById("location").innerHTML = places[place];
    document.getElementById("string").innerHTML = place_states[place][solved[place]];
    document.getElementById("picture").src = "Pictures-" + level + "/" + place + "-" + solved[place] + ".jpg";
    document.getElementById("comment").innerHTML = "";
}
function Start()
{
    var thing = 0;
    var place = 0;
    SetAppearance();
}
function UnlockNextLevel()
{
	var link = document.createElement('a');
	link.appendChild(document.createTextNode("Next Level"));
	link.href = "Level-" + (level + 1) + ".html";
	document.getElementById("next").innerHTML = "";
	document.getElementById("next").appendChild(link);
}
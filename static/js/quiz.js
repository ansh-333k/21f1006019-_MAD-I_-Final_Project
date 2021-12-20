function hide_all()
{
    for (let i = 0; i < 10; i++)
    {
        document.getElementById("question_" + String(i + 1)).style.display = "none";
    }
}

function show(i)
{
    hide_all();
    if (document.getElementById("question_" + String(i + 1)).style.display == "none")
    {
        document.getElementById("question_" + String(i + 1)).style.display = "block";
    }
}

window.onload = function()
{
    show(0);
};
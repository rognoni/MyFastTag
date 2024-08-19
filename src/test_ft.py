from xml import *

def main():
    label = Label(
        "Choose an option", 
        Select(
            Option("one", value="1", selected=True),
            Option("two", value="2", selected=False),
            Option("three", value=3),
            cls="selector",
            _id="counter",
            **{'@click':"alert('Clicked');"},
        ),
        _for="counter",
    )

    print(to_xml(label))

if __name__ == "__main__":
    main()

# Assignment 4

Hyperlink : https://catalogueeee.herokuapp.com/todolist/login <br>

## Essay questions

## What is the difference between Inline, Internal, and External CSS? What are the advantages and disadvantages of each style?

Inline style is a styling method where we immediately insert the style we want to a specific HTML element in its tag. Unlike inline, the internal method involves the style tag in where we would insert our styles into the style tag without having to insert them to each HTML tag individually. Lastly, the external method is where we would make our styles outside of our html file and in another CSS file.<br>
Inline method would be favourable when the html file we are working on only has a few tags and we can immediately insert CSS rules to the HTML files which would make it arguably the fastest if we are doing tests on our page. However, since we need to insert CSS rules to each HTML tags, it would be very time consuming if the number of tags in the html file gets big.<br>
Internal method would be beneficial if we are in a situation where we only need to edit one long html file. By correctly using the class and ID selectors this can make the process of adding CSS rules really easy. Despite that, using the internal method would still be very time consuming if we need to add the rules to a number of html files. In addition to that, by adding the style tag, it may cause our html file size to increase and makes the page load slower.<br>
By using the external method, we can easily add the same rules to a number of files. This is very beneficial as a lot of html files can be linked to the external CSS file and if we make a change to the external CSS file, everything else would also change saving us a lot of time. Also, by simply not adding code to the html file, we can avoid "careless" errors and could save us the trouble of debugging. However, by having an external CSS, it would mean that our page may load slower too as the page might not be loaded correctly until the external CSS is downloaded.

## Describe the HTML5 tags that you know.

"a" makes a hyperlink.
"body" Defines the document's body.
"br" Makes a one line break.
"button" Creates a clickable button.
"style" Specifies style using inline method.
"table" creates a table.
"div" Specifies a divide in the document.


## Describe the types of CSS selectors you know.
- Element selector, selects HTML tags based on their name
- ID selector, Selects elements based on the element's id attribute
- class selector, selects all elements in the same class mentioned
- Universal selector, selects all elements


## Explain how you implement the checklist above.

To complete this assignment, I used the styles from bootstrap and implemented the styles from bootstrap to modify the todolist from last week's assignment. Mostly, I used the internal CSS method where I defined the styles for some of the elements at the head of the documnet using the "style" tag. I also used the inline method to apply CSS rules to some of the elements all of the html files in my templates folder in my todolist application.
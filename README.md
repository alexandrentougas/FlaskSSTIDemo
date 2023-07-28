# SSTI (Server Side Template Injection)

## What the heck is that?

A server-side template injection occurs when an attacker is able to use native template syntax to inject a malicious payload into a template, which is then executed server-side.

## Code example

Here's a simple form in our index.html page:

``` html
<form  id="form"  method="post"  action=""> 
    <label  for="name">Name</label>
    <input  type="text"  name="name"  id="name"  value="" required>
    <button  type="submit">Send</button>
</form>
```
    
![Form](https://github.com/alexandrentougas/FlaskSSTIDemo/blob/main/assets/Form.PNG)

And the data entered is then output like this:

![Output](https://github.com/alexandrentougas/FlaskSSTIDemo/blob/main/assets/Output.PNG)

Let's look at how our form and result are rendered:

``` python
@app.route('/', methods=('GET', 'POST'))
def  index():
    
    if  request.method == 'POST':
	    name = request.form["name"]
	    return  redirect(url_for('result', name=name))
    else:
	    return  render_template('index.html')
  	    
@app.route('/result')  
def  result():
    return  render_template_string(
        "<h1>"+ request.args.get('name') + "</h1>"
    )
```

When the form is submitted, a redirection is made to the **/result URL** by passing it the data entered as the variable **name**.  As we saw in a previous screenshot the URL generated then contains the variable. 

It is then fetched with **request.args.get()** and displayed in a HTML **h1** header. Did you notice how the HTML for the result "page" is written immediately in the python code and not in a HTML template  file? Rendering HTML like this is vulnerable to SSTI.

## Vulnerability example
Let's type something using the syntax of Jinja and  which can be executed as code/logic. The product of 2 numbers for example:

![Form2](https://github.com/alexandrentougas/FlaskSSTIDemo/blob/main/assets/Form2.PNG)

The output ends up being this:

![Output2](https://github.com/alexandrentougas/FlaskSSTIDemo/blob/main/assets/Output2.PNG)

## Safe way of rendering
Let's instead use a result.html page for the rendering of the output. Our page will contain a simple body like that:

``` html
<body>
    <h1>{{ name }}</h1>
</body>
```

And our in our index route we're gonna use our html file instead of redirecting to the result route (which is now useless and can be removed):

``` python
    #return  redirect(url_for('result', name=name)) 
    return render_template('result.html', name=name)
```

If we try to send the same product of numbers, the new output will be:
![Output3](https://github.com/alexandrentougas/FlaskSSTIDemo/blob/main/assets/Output3.PNG)
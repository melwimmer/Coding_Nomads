


def html_p(initial_function):
    def wrapper(text_f):
        html_text = f'<p> {initial_function(text_f)} </p>'
        return html_text
    return wrapper

def html_div(initial_function):
    def wrapper(text_f):
        html_text = f'<div> {initial_function(text_f)} </div>'
        return html_text
    return wrapper


@html_p
def text_func(text):
    return text

txt = "Hii!"

html_txt = text_func(txt)
print(html_txt)


# do the same process with all the html tags. just change <p> and </p>
#If I really wanted, I could make it so that for every new line of a text I would insert a <p>. but I am lazy

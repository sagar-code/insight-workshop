# 10. Write a function that takes camel-cased strings (i.e. ThisIsCamelCased),
# and converts them to snake case (i.e. this_is_camel_cased).
# Modify the function by adding an argument, separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.


def naming_style(string, seperator):
    glue = ' '
    for i in range(1, len(string)):
            string = ''.join(glue + x if x.isupper() else x for x in string).strip(glue).split(glue)
            snake_case = "_".join(string).lower()
            kebab_case = seperator.join(string).lower()
            return snake_case, kebab_case


print(naming_style('ThisIsCamelCased', '-'))
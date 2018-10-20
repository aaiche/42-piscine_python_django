#!/usr/bin/python3

class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        txt = super().__str__()
        txt = txt.replace('<', '&lt;') 
        txt = txt.replace('>', '&gt;') 
        txt = txt.replace('"', '&quot;') 
        txt = txt.replace('\n', '\n<br />\n') 
        return txt

class Elem:
    """
    Elem will permit us to represent our HTML elements.
    Un Element a :
        - <
        - balise=tag
        - des attributs
        - contenu
        - >
    """

    """
    ???? Une sous-classe d’Exception en son sein. ????
    """
    #aa [...]
    class ValidationError(Exception):
        def __init__(self):
            self.message = "This content is not a Text or an Elem."
        def __str__(self):
            return self.message
 
    # 
    # input:
    #   - self      : par defaut - instance elle meme
    #   - tag       : default = div
    #   - attr      : default = {}
    #   - content   : default = None
    #   - tag_type  : tag_type = double
    # 
    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.
        Un constructeur pouvant prendre en paramètre le nom de l’élément, ses attributs
        HTML, son contenu et le type d’élément (balises simples ou doubles).
        """
        #aa [...]
        self.tag = tag
        self.attr = attr
        self.content = []
        if content != None:
            self.add_content(content)
        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        Une méthode __str__() retournant le code HTML de l’élément.
        """
        if self.tag_type == 'double':
            #aa [...]
            result = '<'
            result += self.tag + self.__make_attr()
            result += '>'
            if self.content != None:
                result += self.__make_content()
            result += '</' + self.tag + '>'
        elif self.tag_type == 'simple':
            result = '<' + self.tag  + self.__make_attr() + '>'
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result+= "  " + str(elem).replace('\n', '\n  ') + "\n"
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

if __name__ == '__main__':
    #aa [...]
    #print(str(Elem()))
    #print(Elem(content=Text(1)))
    #assert str(Elem()) == '<div></div>'
    #test_elem_basics()
    #div_elt = Elem(tag = 'div')
    #body_elt = Elem(tag = 'body', attr={}, content = [],tag_type='double')
    #assert str(Elem('div', {}, None, 'double')) == '<div></div>'
    #print(body_elt)

    title_elt = Elem(tag = 'title', content = Text('"Hello ground!"'))

    head_elt = Elem(tag = 'head', content = [title_elt])

    h1_elt = Elem(tag = 'h1', content = Text('"Oh no, not again!"'))
    
    img_elt = Elem(tag = 'img', tag_type = 'simple', attr = {'src': 'http://i.imgur.com/pfp3T.jpg'})

    body_elt = Elem(tag = 'body', content = [h1_elt, img_elt])

    html_elt = Elem(tag = 'html', content = [head_elt, body_elt])
    print(html_elt)


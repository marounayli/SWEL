import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from Levenshtein import distance
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-mpnet-base-v2')


def callmodel(word1, word2):
    try:
        return 0
    except:
        return 0
    # data = {"word1":word1,"word2":word2}
    # res = requests.post("http://localhost:5000/similarity",json=data)
    # return float(res.text)


# generate the xpath of the element
def xpath_soup(element):
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:
        siblings = parent.find_all(child.name, recursive=False)
        components.append(
            child.name
            if siblings == [child] else
            '%s[%d]' % (child.name, 1 + siblings.index(child))
        )
        child = parent
    components.reverse()
    return "/html/body"+'/%s' % '/'.join(components)

# the tag similarity matrix represents how similar each tags are:


tag_sim_matrix = {"button": {"button": 1, "input": 0.75, "p": 0.1, "a": 0.6 , "span":0.5 , "div":0},
                  "p": {"button": 0.1, "input": 0.2, "p": 1, "a": 0.3, "span":0.5, "div":0},
                  "a": {"button": 0.6, "input": 0.2, "p": 0.1, "a": 1, "span":0.5, "div":0},
                  "input": {"button": 0.75, "input": 1, "p": 0.2, "a": 0.2, "span":0.5, "div":0},
                  "span": {"span": 1, "button": 0.5, "input": 0.5, "p": 0.5, "a": 0.5, "div":0},
                  "div":{"div":1,"button":0,"span":0, "a" :0, "input":0,"p":0}}

def calculate_elem_similarity(elt,ref_elt):
    return tag_sim_matrix[elt.name][ref_elt.name]

def LVdistance_values(elt,ref_elt):
    if elt.str and ref_elt.value:
        return 1 - (distance(elt.string,ref_elt.value)/max(len(elt.str),len(ref_elt.value)))
    return 0
    
# def LVdistance_attrs(elt,ref_elt):
#     c=0
#     res = 0 
#     for attr in ref_elt.attrs:
#         if (attr in elt.attrs):
#             c+=1
#             lv_distance = 1- (distance(elt.attrs[attr], ref_elt.attrs[attr]) / max(len(ref_elt.attrs[attr]),len(elt.attrs[attr])))
#             res += lv_distance
#     if c==0:
#         c+=1
#     return res/c

# def calc_sim(elt, ref_elem):
#     res =  calculate_elem_similarity(elt,ref_elem) + LVdistance_values(elt,ref_elem) + LVdistance_attrs(elt,ref_elem)
#     # print(elt.attrs, elt.string, res)
#     return res
    
def calc_sim(elt, ref_elem):
    res = 0
    res += tag_sim_matrix[elt.name][ref_elem.name]
    if elt.string and ref_elem.value:
        lv_distance = distance(elt.string, ref_elem.value)
        if lv_distance == 0:
            lv_distance = 0.5
        res += (0.5*callmodel(elt.string, ref_elem.value) + 0.5*(1/lv_distance))
        embeddings = model.encode([elt.strin , ref_elem.value], convert_to_tensor=True)
        cosine_scores = util.cos_sim(embeddings, embeddings)
        res+=cosine_scores[0][0]*2
    for attr in ref_elem.attrs:
        if (attr in elt.attrs):
            res += (callmodel(elt.attrs[attr], ref_elem.attrs[attr]))
            lv_distance = distance(elt.attrs[attr], ref_elem.attrs[attr])
            if (lv_distance == 0):
                lv_distance = 0.5
            res += 3*(1/lv_distance)
    print(elt.attrs, elt.string, res)
    return 0.1*res


class Elem:
    def __init__(self, name, attrs, value):
        self.name = name
        self.attrs = attrs
        self.value = value


def get_xpath(soup, ref_elt):
    mx = 0
    res = ""
    elts = soup.find_all(lambda tag: tag.name in [
                         'button', 'a', 'p', 'input', 'span' , 'div'])
    eltx = None
    for elt in elts:
        sim = calc_sim(elt, ref_elt)
        if sim > mx:
            mx = sim
            res = xpath_soup(elt)
            eltx = elt
    print("The element is ", eltx, res) 
    return res

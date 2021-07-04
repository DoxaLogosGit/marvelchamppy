import requests
from xml.etree import ElementTree
import math
import time


BASE_URL='https://www.boardgamegeek.com/xmlapi2/'

PLAYS='plays?'
ENTRIES_PER_PAGE=100

def determine_number_of_pages(xml_data):
    """
    given the first play of play data, deterimne how may pages must be retrieved
    note: 100 entries per page
    """
    root = ElementTree.fromstring(xml_data)
    entries = int(root.attrib['total'])
    pages = math.ceil(entries/ENTRIES_PER_PAGE)
    return pages


def retrieve_play_page(url, user, page_num='1'):
    """
    Retrieves the play page given the page number
    returns the xml text
    """
    print("Retrieving page data...")
    res = requests.get(url+PLAYS+"username="+user+"&type=family&page="+page_num)
    print(res)
    if (res.status_code != 200):
        return ""
    else:
        return res.text

def retrieve_play_data_from_bgg(user):
    """
    this the main function to handle retrieve the play data
    from BGG (boardgamegeek) given the base_url and the username
    """
    xml_data = []
    page_data = retrieve_play_page(BASE_URL,user)
    if page_data == "":
        return -1

    pages = determine_number_of_pages(page_data)
    print("Pages of data to retrieve {}".format(pages))

    xml_data.append(page_data)
    #pages = 2 #iterate fast for now
    for index in range(2, pages+1):
        time.sleep(2)
        print("Retrieving page {} of data".format(index))
        page_data = retrieve_play_page(BASE_URL,user,str(index))
        if page_data != "":
            xml_data.append(page_data)

    return xml_data



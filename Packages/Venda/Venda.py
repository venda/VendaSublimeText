import sublime, sublime_plugin
import re

def match(rex, str):
    m = rex.match(str)
    if m:
        return m.group(0)
    else:
        return None

# This responds to on_query_completions, but conceptually it's expanding
# expressions, rather than completing words.
#
# It expands these simple expressions:
# tag.class
# tag#id
class HtmlCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        # Only trigger within HTML
        if not view.match_selector(locations[0],
                "text.html - source - meta.tag, punctuation.definition.tag.begin"):
            return []

        # Get the contents of each line, from the beginning of the line to
        # each point
        lines = [view.substr(sublime.Region(view.line(l).a, l))
            for l in locations]

        # Reverse the contents of each line, to simulate having the regex
        # match backwards
        lines = [l[::-1] for l in lines]

        # Check the first location looks like an expression
        rex = re.compile("([\w-]+)([.#])(\w+)")
        expr = match(rex, lines[0])
        if not expr:
            return []

        # Ensure that all other lines have identical expressions
        for i in xrange(1, len(lines)):
            ex = match(rex, lines[i])
            if ex != expr:
                return []

        # Return the completions
        arg, op, tag = rex.match(expr).groups()

        arg = arg[::-1]
        tag = tag[::-1]
        expr = expr[::-1]

        if op == '.':
            snippet = "<{0} class=\"{1}\">$1</{0}>$0".format(tag, arg)
        else:
            snippet = "<{0} id=\"{1}\">$1</{0}>$0".format(tag, arg)

        return [(expr, snippet)]


# Provide completions that match just after typing an opening angle bracket
class TagCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        # Only trigger within HTML
        if not view.match_selector(locations[0],
                "text.html - source"):
            return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        if ch != '<':
            return []

        return ([
             #Start of Venda Tags
             #this is for the context menu selection of the tags. Requires user open the tag with <
            ("venda_category\tVenda Tag", "venda_category temp=${1:'insert value'},ref=${2:'insert value'},rec${3:=icat}${4:=scat}${5:=pcat}${6:=elementcat}, ivtype=${7:'insert value'}>"),
            ("venda_category -bklist only\tVenda Tag", "venda_category bklist=${0:'enter value'}>"),
            ("venda_dateformat\tVenda Tag", "venda_dateformat type${1:=long}${2:=short}${3:=digit},format${4:=dd/mm/yyyy}${5:=dd mm yyyy},suffix=${6:'insert value'},date${7:=dd-mm-yyyy}${8:=yyyy-mm-dd}${9:=now}>"),
            ("venda_entmediaadd\tVenda Tag", "venda_entmediaadd>"),
            ("venda_ebizurl\tVenda Tag", "venda_ebizurl>"),
            ("venda_bsref\tVenda Tag", "venda_bsref>"),
            ("venda_pageadd\tVenda Tag", "venda_pageadd alt=\"${0:insert value}\">"),
            ("venda_cattree\tVenda Tag", "venda_cattree class=${0:'insert value'},sep=${1:'insert value'},append=${2:'insert value'}>"),
            ("venda_detblock\tVenda Tag", "venda_detblock>${0:'insert value'}</venda_detblock>"),
            ("venda_dispview -invt\tVenda Tag", "venda_dispview invt=${0:'insert value'}>"),
            ("venda_dispview -page\tVenda Tag", "venda_dispview page=${0:'insert value'}>"),
            ("venda_dispview -pcat\tVenda Tag", "venda_dispview pcat=${0:'insert value'}>"),
            ("venda_dispview -stry\tVenda Tag", "venda_dispview stry=${0:'insert value'}>"),
            ("venda_dispview -scat\tVenda Tag", "venda_dispview scat=${0:'insert value'}>"),
            ("venda_dispview -icat\tVenda Tag", "venda_dispview icat=${0:'insert value'}>"),
            ("venda_extflds\tVenda Tag", "venda_extflds exfldtype${1:=order}${2:=orderitem},group=${3:'insert text'},template${4:=oixtDisplay}${5:=orxtDisplay}${6:=pdxtDisplay}${7:=extflds},type${8:=emailincludes}${9:=exfields/order}${10:=exfields/orderitem},ref=$11,displayonly=$12>"),
            ("venda_hashtags\tVenda Tag", "venda_hashtags>"),
            ("venda_inctemplate\tVenda Tag", "venda_inctemplate name=${1:'insert name'}, type${2:=emailincludes}${3:=exfields/user}${4:=includes}${5:=includes/tracking}${6:=invt}${7:=mainincludes}${8:=search}${9:=vbm}${10:=widgets}>"),
            ("venda_inventory\tVenda Tag", "venda_inventory ref=${0:'insert ref'},temp=${1:'insert template'},displayunpublished=${2:'insert value'}>"),
            ("venda_invtacc\tVenda Tag", "venda_invtacc template=${0:'insert template'}>"),
            ("venda_invtref\tVenda Tag", "venda_invtref>"),
            ("venda_invtsub\tVenda Tag", "venda_invtsub template=${0:'insert template'}>"),
            ("venda_mediagrid\tVenda Tag", "venda_mediagrid template=${0:'insert template'}>"),
            ("venda_media\tVenda Tag", "venda_media icat${2:=invt}${3:=scat}${4:=pcat}${5:=stry},type${6:=pict}${7:=movie}${8:=sound}${9:=sound}${10:=pict-movie-sound},key${11:=anyvalue}${12:=multi},img=${13:'insert value'}>"),
            ("venda_page\tVenda Tag", "venda_page page=${0:'insert page'}>"),
            ("venda_setting\tVenda Tag", "venda_setting type=ebiz,name=${0:'insert name'}>"),
            ("venda_text\tVenda Tag", "venda_text id=${0:'insert id'}>"),
            ("venda_tpcomment\tVenda Tag", "venda_tpcomment><!-- $1--></venda_tpcomment>"),
            ("venda_tpxt\tVenda Tag", "venda_tpxt mode=${0:'insert mode'},name=${1:'insert name'},value=${2:'insert value'}>"),
            ("venda_detail\tVenda Tag", "venda_detail>"),
            ("venda_wizbutton\tVenda Tag", "venda_wizbutton step=${0:'insert step'},param1=${0:'insert param1'},wizard=${0:'insert wiz'},mode=${0:'insert mode'},callonly=${0:'insert callonly'}>"),
            ("venda_pagination\tVenda Tag", "venda_pagination template=${0:'insert template'}>"),
            ("venda_listrecords\tVenda Tag", "venda_listrecords cookie=${0:'insert cookie'},temp=${1:'insert template'},limit=${2:'insert limit'}>"),
            ("venda_userinfo\tVenda Tag", "venda_userinfo></venda_ userinfo>"),
            ("venda_ustype\tVenda Tag", "venda_ustype>"),
            ("venda_sessionlanguage\tVenda Tag", "venda_sessionlanguage>"),
            ("venda_sessionlocation\tVenda Tag", "venda_sessionlocation>"),
            ("venda_addedmsg\tVenda Tag", "venda_addedmsg msg=${0:'insert message'}>"),
            ("venda_protocol\tVenda Tag", "venda_protocol>"),
            ("venda_workflow\tVenda Tag", "venda_workflow>"),
            ("venda_story\tVenda Tag", "venda_story template=${1:'insert template'},story=${2:'insert story'}>"),
            ("venda_zone\tVenda Tag", "venda_zone type${0:=countrygroups}${1:=countries}${2:=states},template=${3:'insert template'},parent=${4:'insert parent'},region=${5:'insert region'},isdeliverable=${6:'insert deliverable'}>")

        ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
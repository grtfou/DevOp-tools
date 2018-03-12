##### Changed template style

### Changed CSS style
```
main folder         template name (ex. dokuwiki)
[dokuwiki/conf/tpl/<new_template_name>]
       |-[css]
       |   |- basic.less   # your new css file
       |   |- ...
       |
       |-style.ini
```

```bash
$ mkdir -p dokuwiki/conf/tpl/<new_template_name>/css/
# copy default file to edit your new style (ex. basic.less)
$ cp dokuwiki/lib/tpl/dokuwiki/css/basic.less  dokuwiki/conf/tpl/<new_template_name>/css/
$ vim dokuwiki/conf/tpl/<new_template_name>/css/basic.less
```

### About style.ini
```
; Ref: https://www.dokuwiki.org/devel:style.ini
[stylesheets]
css/basic.less      = screen  ; prefix: dokuwiki/conf/tpl/<new_template_name>/
css/content.less    = screen

[replacements]
__site_width__      = "90%"   ; Replace default value in style.ini
```

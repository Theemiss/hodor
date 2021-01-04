# hodor


## Descreption 
Multiple Script that vote in specific website for my school id Using Selenuim module in the level 1 and 0

### level_0
 * vote 1024 to your school id
### level_1
* vote 4096 to your school id

## Requirment:
 * Google Chrome: need Google Chrome installed in your computer
 * Chrome Driver (need to be the same version of you chrome you have in your computer)
 you can use other navigator like Firefox ...,also you will need the geekoDriver if you chose Firefox
 
 * In Case you chose Firefox change lines in the Script
 ```
 path = cwd + "/geekodriver"
driver = webdriver.Firefox
```
and make the necessary changes

## Usage Example : Level 0
```
> ./script.py
```
## output : : Level 0
```
1 Vote
2
.
.
.
.
1024 vote
```
the script will take 1024S to complete . Duo The Wait Bridge i put in case Your internet is Slow as Hell 

So Dosent crush ("Element not found")

Same Goes for All Scripts
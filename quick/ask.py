import google.generativeai as genai
import os
import re
from PIL import Image
from time import sleep
# print imports
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
# prompt imports
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.validation import Validator
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.application.current import get_app
from prompt_toolkit.enums import EditingMode
from prompt_toolkit.cursor_shapes import CursorShape, ModalCursorShapeConfig

# set model
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
#model = genai.GenerativeModel('models/gemini-pro')
chat = model.start_chat(history=[])

rconsole = Console()
keybindings = KeyBindings()

@keybindings.add('c-x')
def _(event):
    print(" Exit when `c-x` is pressed. ")
   

@keybindings.add('c-space')
def _(event):
    " Initialize autocompletion, or select the next completion. "
    buff = event.app.current_buffer
    if buff.complete_state:
        buff.complete_next()
    else:
        buff.start_completion(select_first=False)

@keybindings.add('f5')
def _(event):
	" Toggle between Emacs and Vi mode. "
	app = event.app

	if app.editing_mode == EditingMode.VI:
		app.editing_mode = EditingMode.EMACS
	else:
		app.editing_mode = EditingMode.VI
          

# cursor switching          
CURSORS = (
    CursorShape.UNDERLINE,
    CursorShape.BLINKING_UNDERLINE,
    CursorShape.BLOCK,
    CursorShape.BLINKING_BLOCK,
    CursorShape.BEAM,
    CursorShape.BLINKING_BEAM,
)
CURSOR_IDX=4
@keybindings.add('f6')
def _(event):
	global CURSOR_IDX, CURSORS
	CURSOR_IDX += 1 
	promptSession.cursor = CURSORS[CURSOR_IDX % len(CURSORS)]
            
             
# Add a toolbar at the bottom to display the current input mode.
def bottom_toolbar():
	" Display the current input mode. "
	edit_mode = 'Vi' if get_app().editing_mode == EditingMode.VI else 'Emacs'
	cursor = promptSession.cursor
	return [
		('class:toolbar', ' [F5] %s' % edit_mode),
		('class:toolbar', ' [F6] %s' % cursor)
	]


# regex
PATTERNS = [
	# * **Smart homes:**
	# (r"\* \*\*(.*?):\*\*", r"\t\1\n\t\n"), # h2

	# (r"\*\*(.*?):\*\*",   r"\t\t\1"), # h3
	
 	# **Some examples of IoT applications:**
	(r"\*\*(.*?):\*\*",    r"\n\1\n====================================\n\n") # h1 
]
IMG_PATTERN = r"@image\s*\(([^)]+)\)"  # Matches "@image(", then captures the path, then matches ")"


def ask(text:str, stream:bool=False):
    
	response = model.generate_content(text, stream=stream)
	if stream:
		for chunk in response:
			print_colored_text(text=chunk.text, color="white")
	else:
		print_colored_text(text=response.text, color="white")
		
def rmv_signs(text:str):
    
    signs = """,.?\\*+-/!:|\" \n\'<>\0"""
    for c in signs:
        text = text.replace(c, '_')
    return text
    
def run_chat(qst:str, stream:bool=False):
	global chat
	
	ing_path = None
	response = None
	with rconsole.status("please, hold on...", spinner="bouncingBall"):
		try:	
			# retrieve the image path from the request message
			match_img = re.search(IMG_PATTERN, qst)
			if match_img:
				img_path = match_img.group(1).strip() # Extract the captured path and remove leading/trailing whitespace
				qst = re.sub(pattern=IMG_PATTERN, repl="", string=qst) # removes the image path from qst
			    # Send Question and Image
            # Send Question, No image
			response = chat.send_message([qst, Image.open(img_path)] if match_img else qst, stream=stream)
		except Exception as e:
			rconsole.print(f"[i]{e}[/i] :smiley:", style="bold red")
			return

	with rconsole.pager(): # .status("writing...", spinner="bouncingBall"):
		rconsole.print(Figlet(font="bigfig").renderText(f"Response: {len(chat.history) + 1}"), style="bold green")
		text = response.text
		# for pattern, replacement in PATTERNS: # work on the text
			# text = re.sub(pattern=pattern, repl=replacement, string=text)

		file_name = rmv_signs(text=qst[:100])
		with open(".ask_history/"+file_name+".txt", encoding="utf-8", mode="w") as file:
			file.write(f"{qst}\n{text}")

		rconsole.print(text, style="bold white")
	
	rconsole.print(text, style="bold white")
			

def print_colored_text(text, color):
    colors = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
    }

    print(colors[color] + text + "\033[0m")


def is_empty(text:str):
	return not (len(text) == 0 or text.replace(" ", "") == "")


promptSession  = None
triggers = ['@go', '@exit', '@history', '@profile', '@help', '@image(path/to/the/image)']
def main():
    
    def prompt_continuation(width, line_number, is_soft_wrap):
        return ' ' * width
    	# Or: return [('', '.' * width)]
    
    global wordCompleter
    wordCompleter = WordCompleter(triggers)
    validator = Validator.from_callable(
								is_empty,
								error_message="Empty prompt ignored, Please say something",
								move_cursor_to_end=True
    )
    global promptSession
    promptSession = PromptSession(completer=wordCompleter,
                         	complete_while_typing=True,
                          	validator=validator,
							vi_mode=False,
							key_bindings=keybindings,
							bottom_toolbar=bottom_toolbar,
       						prompt_continuation=prompt_continuation,
							mouse_support=True,
							cursor=CursorShape.BLINKING_BEAM,
                          	# history=FileHistory('~/.ask_genai_history')
	)
 

def handle_cmd(cmd:str):

	pass
	
 
if __name__=="__main__":
    
	main()	
	# Rules table
	print(Figlet().renderText("n j a d - AI"))
	rconsole.print("Welcome to njad-term-genai. this is a Gemini-powered console app.",
                "\n>>Type your multi-line text in prompt below then press [i]Shift[/i] then [i]ENTER[/i].",
                "\n>>You can type [i][u]@help[/i][/u] to see useful commands.",
                "\n>>To include an image anywhere in the text, follow the pattern: [i][u]@image(absolute path to your image)[/i][/u]",
				"\nEXAMPLE: explain how blockchain works in 10 paragraphs. do refer to the image @image(/home/me/Downloads/test.png), and explain it with easy words.",
                  	style="bold magenta")

	while True:

		rconsole.print(Figlet(font="bigfig").renderText(f"Prompt: {len(chat.history)//2+1}"), style="bold green")
		try:
			# read multiline input: press Ctrl+D (UNIX), Ctrl+Z (windows) to set EOF (stop)
			text:str = promptSession.prompt(message="> ", multiline=True)
			cmd = text.replace(' ', '').replace('\n', '') 	

			# process prompt
			try:
				if cmd in triggers: 
					if cmd == "/exit": print("bye-bye"); break; exit(0);
					else: handle_cmd(cmd=cmd);
         
				else: run_chat(qst=text, stream=False);
			except Exception as e:
				rconsole.print(f"[red]Sorry, An Error Occured! [white][i]{e}[/i]", style="bold")

		except KeyboardInterrupt:
			print("Bye-bye.")
			exit(0)

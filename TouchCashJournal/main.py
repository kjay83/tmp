# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from typing import List, Dict
import datetime
import json

# CONSTANT DEFINITIONS
app_name = 'TOUCH'
separator = ","
basic_help = (f"Save your expenses and revenues with {app_name}. "
              "Enter 'h' ou 'help' to show help. "
              "Enter 'm' ou 'menu' to show general enu. ")
complete_help1 = (
    """The app save all the operations you enter and update the accounts total amounts.
    An operation format is like '+2000,salary' or '-200,star bucks'
    You enter first the SYMBOL operation then the AMOUNT follow by the SEPARATOR 
    then the DESCRIPTION."""
)
complete_help2 = (f"The actual SEPARATOR is '{separator}' so remember "
                  f"[SYMBOL][AMOUNT][SEPARATOR][DESCRIPTION]")
complete_help = complete_help1 + complete_help2
operation_nb_terms = 2
default_account: str = "CASH"
accounts: Dict = {default_account: 0}
selected_account: str = default_account
app_version_number = "1.0"
prompt_line = f"({app_name} V{app_version_number})-[{default_account}: 0 XAF]>>> "
# to save imediatly after each transaction in the session
auto_save_transactions_in_session = True
# to save transactions history in journal file before quitting ap
auto_save_history_in_journal_before_quit = True
# to save all accounts info file before quitting ap
auto_save_accounts_in_file_before_quit = True
session_operations_history: List = []
accounts_operations_history: List = []
history_file_separator = ';'
operations_journal_file_name = "operations_journal.json"
accounts_file_name = "accounts.json"
classic_press_enter_input = "--Press ENTER--"


# GENERAL MENU CONSTANT
class Menus:
    HELP_SHORTCUT1 = "H"
    HELP_COMPLETE_LETTERS = "HELP"
    QUIT_SHORTCUT1 = "Q"
    QUIT_COMPLETE_LETTERS = "QUIT"
    GENERAL_SHORTCUT1 = "M"
    GENERAL_COMPLETE_LETTERS = "MENU"
    HISTORY_COMPLETE_LETTERS = "HISTORY"
    JOURNAL_SHORTCUT1 = "J"
    JOURNAL_COMPLETE_LETTERS = "JOURNAL"
    LOAD_SHORTCUT1 = "L"
    LOAD_COMPLETE_LETTERS = "LOAD"
    SAVE_COMPLETE_LETTERS = "SAVE"


def make_history_line(operation_string, account_name) -> str:
    # format : date;CASH;-1000,ju
    operation_datetime = datetime.datetime.now()
    return f"{operation_datetime}{history_file_separator}{account_name}{history_file_separator}{operation_string}"


def update_session_history(operation_string: str) -> None:
    if auto_save_transactions_in_session:
        line = make_history_line(operation_string, selected_account)
        session_operations_history.insert(0, line)


def save_session_operations():
    if len(session_operations_history) > 0:
        # getting accounts operations history
        load_history_from_file()
        # adding old transactions to current session history
        if len(accounts_operations_history) > 0:
            for old_ope in accounts_operations_history:
                session_operations_history.append(old_ope)

        # Serializing json
        json_object = json.dumps(session_operations_history, indent=4, ensure_ascii=True)
        with open(operations_journal_file_name, "w") as f:
            f.write(json_object)


def save_accounts():
    if len(accounts) > 0:
        # Serializing json
        json_object = json.dumps(accounts, indent=4, ensure_ascii=True)
        # this file is always erased anew
        with open(accounts_file_name, "w") as f:
            f.write(json_object)


def update_selected_account_after_load():
    account_names: List = list(accounts.keys())
    if default_account not in account_names:
        selected_account = account_names[0]
        print(f"!! Selected Account is now {selected_account}")


def load_accounts_from_file():
    # Opening JSON file
    try:
        with open(accounts_file_name, 'r') as f:
            # Reading from json file
            json_object: Dict = json.load(f)
            if json_object is not None and len(json_object) > 0:
                accounts.clear()
                for key, val in json_object.items():
                    accounts.update({key: val})
                update_selected_account_after_load()
    except FileNotFoundError:
        print(f"File {accounts_file_name} does not exist")


def load_history_from_file():
    # Opening JSON file
    try:
        with open(operations_journal_file_name, 'r') as f:
            # Reading from json file
            json_object = json.load(f)
            if json_object is not None and len(json_object) > 0:
                accounts_operations_history.clear()
                for op in json_object:
                    accounts_operations_history.append(op)
    except FileNotFoundError:
        print(f"File {operations_journal_file_name} does not exist")


def get_updated_prompt_line() -> str:
    return f"({app_name} V{app_version_number})-[{selected_account}: {accounts[selected_account]} XAF]>>> "


def show_help():
    print(complete_help1)
    input(classic_press_enter_input)
    print(complete_help2)
    input(classic_press_enter_input)


def account_amount_add(account_name: str = default_account, new_amount: float = 0) -> None:
    account_total = accounts.get(account_name)
    if account_total is None:
        error_msg = f"ERROR: The account {account_name} doesn't exist to add {new_amount}"
        print(error_msg)
    else:
        accounts.update({account_name: account_total + new_amount})


def account_amount_substract(account_name: str = default_account, new_amount: float = 0) -> None:
    account_total = accounts.get(account_name)
    if account_total is None:
        error_msg = f"ERROR: The account {account_name} doesn't exist to substract {new_amount}"
        print(error_msg)
    else:
        if account_total == 0:
            error_msg = f"ERROR: The account {account_name} is already EMPTY (Total amount = 0)!"
            print(error_msg)
        else:
            result = account_total - new_amount
            if result < 0:
                error_msg = f"ERROR: You cannot substract {new_amount} from {account_total}!"
                print(error_msg)
            else:
                accounts.update({account_name: result})


def update_account_supposing_valid_operation_string(operation_string: str):
    # format desired examples: "-5000,night club" "+100000, salary"..
    # the operation string is supposed to be valid
    operation_string_splitted = operation_string.split(separator)
    amount_string = operation_string_splitted[0]
    amount_description = operation_string_splitted[1]
    operation_symbol = amount_string[0]
    # print(f"in update {amount_string[1:]}")
    true_amount = float(amount_string[1:])
    # success_msg = "Successfully updated account"
    match operation_symbol:
        case '+':
            account_amount_add(selected_account, true_amount)
        case '-':
            account_amount_substract(selected_account, true_amount)
    # print(success_msg)


def is_valid_operation_symbol(symbol: str) -> bool:
    # check if the symbol is for an accepted update operation
    result = False
    if symbol is not None and len(symbol) == 1:
        if symbol == '+' or symbol == '-':
            result = True
    return result


def is_valid_amount_string(amount_string: str) -> bool:
    result = False
    # this string is to be symbol then number
    # # for example '+5000' or '-100000'
    if amount_string is not None and len(amount_string) > 1:
        # checking symbols
        symbol = amount_string[0]
        true_amount = amount_string[1:]
        if is_valid_operation_symbol(symbol) and true_amount.isnumeric():
            result = True

    return result


def is_valid_operation(operation_string: str) -> bool:
    # check if the operation is valid ie conform to attended format
    #
    result = False
    if operation_string is not None and len(operation_string) > 0:
        terms = operation_string.split(separator)
        if len(terms) == operation_nb_terms:
            # format desired examples: "-5000,night club" "+100000, salary"..
            amount_string = terms[0]
            if is_valid_amount_string(amount_string):
                result = True
    return result


def is_valid_operation_with_error_msg(operation_string: str) -> bool:
    # check if the operation is valid ie conform to attended format
    # and print a error msg if not
    result = False
    error_msg = ("Bad format entry. "
                 "Use [operation symbol][amount][separator][description] "
                 "instead or 'h' for help")
    if is_valid_operation(operation_string):
        result = True
    else:
        print(error_msg)
    return result


def print_operations_list(op_list: List) -> None:
    header_string = "(LINE NUMBER) DATE;ACCOUNT NAME;AMOUNT;DESCRIPTION"
    if len(op_list) > 0:
        print(f"{header_string}")
        nb_operations = len(op_list)
        for i in range(nb_operations):
            old_operation = op_list[i]
            print(f"({nb_operations - i}) {old_operation}")
        input(classic_press_enter_input)
    else:
        print("The operation list is empty")


def show_session_operations_history():
    print("showing all operations in actual session:")
    print_operations_list(session_operations_history)


def show_general_menu():
    print(f"Enter 'h' or 'HELP' for HELP ")
    print(f"Enter 'm' or 'MENU' for this menu ")
    print(f"Enter 'HISTORY' to show the operations entered in current session")
    print(f"Enter 'j' or 'JOURNAL' to read the operations journal from file")
    print(f"Enter 'SAVE' to save operations history in file")
    print(f"Enter 'q' or 'QUIT' to exit TOUCH app")


def quit_app():
    if auto_save_history_in_journal_before_quit:
        save_session_operations()
    if auto_save_accounts_in_file_before_quit:
        save_accounts()
    sys.exit(0)


def show_save_menu():
    save_session_operations()
    session_operations_history.clear()
    print(
        "All operations in this session have been added to the journal. The session history is now empty.")
    save_accounts()
    print("All accounts info have been saved in file.")


def show_journal_menu():
    load_history_from_file()
    print(f"Showing the content of journal.")
    print_operations_list(accounts_operations_history)


def show_load_menu():
    load_accounts_from_file()
    if len(accounts) > 0:
        print(f"The accounts have been successfully loaded.")
    else:
        print(f"The file {accounts_file_name} was empty or not conform. No data loaded.")


def start_app():
    while True:
        command_entered = input(get_updated_prompt_line()).upper()
        match command_entered:
            case Menus.HELP_SHORTCUT1 | Menus.HELP_COMPLETE_LETTERS:
                show_help()
            case Menus.GENERAL_SHORTCUT1 | Menus.GENERAL_COMPLETE_LETTERS:
                show_general_menu()
            case Menus.HISTORY_COMPLETE_LETTERS:
                show_session_operations_history()
            case Menus.JOURNAL_SHORTCUT1 | Menus.JOURNAL_COMPLETE_LETTERS:
                show_journal_menu()
            case Menus.LOAD_SHORTCUT1 | Menus.LOAD_COMPLETE_LETTERS:
                show_load_menu()

            case Menus.SAVE_COMPLETE_LETTERS:
                show_save_menu()
            case Menus.QUIT_SHORTCUT1 | Menus.QUIT_COMPLETE_LETTERS:
                quit_app()
            case _:
                if is_valid_operation_with_error_msg(command_entered):
                    update_account_supposing_valid_operation_string(command_entered)
                    update_session_history(command_entered)
                else:
                    print(basic_help)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_app()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

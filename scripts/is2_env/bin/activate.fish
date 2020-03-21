<<<<<<< HEAD
# This file must be used using `. bin/activate.fish` *within a running fish ( http://fishshell.com ) session*.
# Do not run it directly.

function deactivate -d 'Exit virtualenv mode and return to the normal environment.'
    # reset old environment variables
    if test -n "$_OLD_VIRTUAL_PATH"
        set -gx PATH $_OLD_VIRTUAL_PATH
=======
# This file must be used using `source bin/activate.fish` *within a running fish ( http://fishshell.com ) session*.
# Do not run it directly.

function _bashify_path -d "Converts a fish path to something bash can recognize"
    set fishy_path $argv
    set bashy_path $fishy_path[1]
    for path_part in $fishy_path[2..-1]
        set bashy_path "$bashy_path:$path_part"
    end
    echo $bashy_path
end

function _fishify_path -d "Converts a bash path to something fish can recognize"
    echo $argv | tr ':' '\n'
end

function deactivate -d 'Exit virtualenv mode and return to the normal environment.'
    # reset old environment variables
    if test -n "$_OLD_VIRTUAL_PATH"
        # https://github.com/fish-shell/fish-shell/issues/436 altered PATH handling
        if test (echo $FISH_VERSION | head -c 1) -lt 3
            set -gx PATH (_fishify_path "$_OLD_VIRTUAL_PATH")
        else
            set -gx PATH "$_OLD_VIRTUAL_PATH"
        end
>>>>>>> e13e650958cc4f04655f013dc5a92bc33fd584d8
        set -e _OLD_VIRTUAL_PATH
    end

    if test -n "$_OLD_VIRTUAL_PYTHONHOME"
<<<<<<< HEAD
        set -gx PYTHONHOME $_OLD_VIRTUAL_PYTHONHOME
=======
        set -gx PYTHONHOME "$_OLD_VIRTUAL_PYTHONHOME"
>>>>>>> e13e650958cc4f04655f013dc5a92bc33fd584d8
        set -e _OLD_VIRTUAL_PYTHONHOME
    end

    if test -n "$_OLD_FISH_PROMPT_OVERRIDE"
<<<<<<< HEAD
=======
       and functions -q _old_fish_prompt
>>>>>>> e13e650958cc4f04655f013dc5a92bc33fd584d8
        # Set an empty local `$fish_function_path` to allow the removal of `fish_prompt` using `functions -e`.
        set -l fish_function_path

        # Erase virtualenv's `fish_prompt` and restore the original.
        functions -e fish_prompt
        functions -c _old_fish_prompt fish_prompt
        functions -e _old_fish_prompt
        set -e _OLD_FISH_PROMPT_OVERRIDE
    end

    set -e VIRTUAL_ENV

    if test "$argv[1]" != 'nondestructive'
        # Self-destruct!
        functions -e pydoc
        functions -e deactivate
<<<<<<< HEAD
=======
        functions -e _bashify_path
        functions -e _fishify_path
>>>>>>> e13e650958cc4f04655f013dc5a92bc33fd584d8
    end
end

# Unset irrelevant variables.
deactivate nondestructive

<<<<<<< HEAD
set -gx VIRTUAL_ENV "/home/giuli/Desktop/pythonprojects/project-item-management-system/scripts/is2_env"

set -gx _OLD_VIRTUAL_PATH $PATH
set -gx PATH "$VIRTUAL_ENV/bin" $PATH
=======
set -gx VIRTUAL_ENV '/home/nelson/Escritorio/project-item-management-system/scripts/is2_env'

# https://github.com/fish-shell/fish-shell/issues/436 altered PATH handling
if test (echo $FISH_VERSION | head -c 1) -lt 3
   set -gx _OLD_VIRTUAL_PATH (_bashify_path $PATH)
else
    set -gx _OLD_VIRTUAL_PATH "$PATH"
end
set -gx PATH "$VIRTUAL_ENV"'/bin' $PATH
>>>>>>> e13e650958cc4f04655f013dc5a92bc33fd584d8

# Unset `$PYTHONHOME` if set.
if set -q PYTHONHOME
    set -gx _OLD_VIRTUAL_PYTHONHOME $PYTHONHOME
    set -e PYTHONHOME
end

function pydoc
    python -m pydoc $argv
end

if test -z "$VIRTUAL_ENV_DISABLE_PROMPT"
    # Copy the current `fish_prompt` function as `_old_fish_prompt`.
    functions -c fish_prompt _old_fish_prompt

    function fish_prompt
<<<<<<< HEAD
        # Save the current $status, for fish_prompts that display it.
        set -l old_status $status

        # Prompt override provided?
        # If not, just prepend the environment name.
        if test -n ""
            printf '%s%s' "" (set_color normal)
=======
        # Run the user's prompt first; it might depend on (pipe)status.
        set -l prompt (_old_fish_prompt)

        # Prompt override provided?
        # If not, just prepend the environment name.
        if test -n ''
            printf '%s%s' '' (set_color normal)
>>>>>>> e13e650958cc4f04655f013dc5a92bc33fd584d8
        else
            printf '%s(%s) ' (set_color normal) (basename "$VIRTUAL_ENV")
        end

<<<<<<< HEAD
        # Restore the original $status
        echo "exit $old_status" | source
        _old_fish_prompt
=======
        string join -- \n $prompt # handle multi-line prompts
>>>>>>> e13e650958cc4f04655f013dc5a92bc33fd584d8
    end

    set -gx _OLD_FISH_PROMPT_OVERRIDE "$VIRTUAL_ENV"
end

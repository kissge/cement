"""These methods and classes controller how commands are parsed and run."""

import re

from cement import namespaces
from cement.core.log import get_logger
from cement.core.hook import run_hooks
from cement.core.opt import parse_options
from cement.core.configuration import set_config_opts_per_cli_opts
from cement.core.exc import CementArgumentError

log = get_logger(__name__)
        
# FIXME: This method is so effing ugly.
def run_command(cmd_name=None):
    """
    Run the command or namespace-subcommand as defined by the 'expose()'
    decorator used on a Controller function.
    
    Keyword arguments:
    cmd_name --  The command name as store in the global 'namespaces'.  For
                 example, namespaces['global'].commands['cmd_name'].
                
    """
    log.debug("processing passed command '%s'", cmd_name)
    cmd_name = cmd_name.rstrip('*') 
    if cmd_name in namespaces.keys():
        namespace = cmd_name
    else:
        namespace = 'global'
    
    m = re.match('(.*)-help', cmd_name)
    if m and m.group(1) in namespaces.keys():   
        namespace = m.group(1)
        raise CementArgumentError, \
            "'%s' is a namespace*, not a command.  See '%s --help' instead." % \
                (namespace, namespace)
        
    (cli_opts, cli_args) = parse_options(namespace=namespace)
    if namespace == 'global':
        set_config_opts_per_cli_opts('global', cli_opts)
    else:
        # if it merges in global ooptions, then it overrites them too.
        if  namespaces[namespace].config.has_key('merge_global_options') and \
            namespaces[namespace].config['merge_global_options']:
            set_config_opts_per_cli_opts('global', cli_opts)    
        set_config_opts_per_cli_opts(namespace, cli_opts)
    
    # FIX ME: need a global_pre_command_hook here so that clibasic can
    # look for -C and if so, parse the passed config files into the dict.
    for res in run_hooks('post_options_hook', cli_opts, cli_args):
        pass # doesn't expect a result
    
    if namespace == 'global':
        actual_cmd = cmd_name
    else:
        try:
            actual_cmd = cli_args[1]
        except IndexError:
            raise CementArgumentError, "%s is a namespace* which requires a sub-command.  See '%s --help?" % (namespace, namespace)
    
    # jsonify it
    if cli_opts.enable_json:
        actual_cmd = "%s.json" % actual_cmd
        
    if namespaces[namespace].commands.has_key(actual_cmd):
        func = namespaces[namespace].commands[actual_cmd]['func']
        log.debug("executing command '%s'" % actual_cmd)
        func(cli_opts, cli_args)
    else:
        raise CementArgumentError, "Unknown command '%s', see --help?" % actual_cmd
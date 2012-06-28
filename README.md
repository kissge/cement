
NAME: Cement

AUTHOR: BJ Dierkes <wdierkes@5dollarwhitebox.org>

DESCRIPTION:

Cement is an advanced CLI Application Framework for Python, and a complete
rewrite of Cement version 0.x/1.x.  Its goal is to introduce a standard, and 
feature-full platform for both simple and complex command line applications as 
well as support rapid development needs without sacrificing quality.

Cement core features include (but are not limited to):

    * Core pieces of the framework are customizable via handlers/interfaces
    * Extension handler interface to easily extend framework functionality
    * Config handler supports parsing multiple config files into one config
    * Argument handler parses command line arguments and merges with config
    * Log handler supports console and file logging
    * Plugin handler provides an interface to easily extend your application
    * Hook support adds a bit of magic to apps and also ties into framework
    * Handler system connects implementation classes with Interfaces
    * Output handler interface renders return dictionaries to console
    * Cache handler interface adds caching support for improved performance
    * Core library and extensions have zero external dependencies*
    * Extensions with external dependencies packaged separately
    * Controller handler supports sub-commands, and nested controllers
    * 98% Nose test coverage
    * Extensive Sphinx documentation
    * Tested on Python 2.6, 2.7, 3.1, and 3.2
    
Cement extensions include:

    * JSON output handler extension (adds --json option)
    * YAML output handler extension (adds --yaml option)
    * ConfigObj config handler extension replaces ConfigParser
    * Daemon extension handles background processes (adds --daemon option)
    * Genshi output handler extension provides Text Templating
    * Memcached cache handler extension provides easy caching

*Note that argparse is required as an external dependency for Python < 2.7 
and < 3.2.  Some extensions rely on external dependencies.*


MORE INFORMATION:

All documentation is available from the official website:

    http://builtoncement.org
    
    
LICENSE:

The Cement CLI Application Framework is Open Source and is distributed under 
the BSD License (three clause).  Please see the LICENSE file included with 
this software.  
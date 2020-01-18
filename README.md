# baidu-transl

This is a command line tool for [baidu translation](https://fanyi.baidu.com/).

## Installation

``` shell
pip3 install .
```

## Usage

``` shell
bdtrans run <content to be translated> [options]
```

If no options are provided, it will translate English into Chinese. For all available options please take a look at [Options Part](#options).

**NOTE:** Before running the command line tool, please register an account in this [website](https://api.fanyi.baidu.com/). You need to provide an id and a password in order to call the baidu API. The id and password will be saved in your local storage.

### Options

``` shell
Options:
  -f, --from TEXT  srouce language
  -t, --to TEXT    target language
  --help           Show this message and exit.
```

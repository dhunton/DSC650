# macOS

!!! warning "Documentation in Progress"
    Check back soon for more updates.
    
--- 

## Package Manager

If you are using macOS as your primary development environment, I recommend using a package manager like [homebrew][homebrew]. 

A package manager is a tool that automates the process of installing, updating, configuring, and removing computer programs. Package managers are commonly used on Unix and Linux distributions. Debian Linux systems, like Ubuntu, use `aptitude`. Red Hat and Fedora systems use `yum`.  `MacPorts` and `homebrew` are two popular package managers for macOS. `Chocolatey` is a popular package manager for Windows. 

You can install Homebrew on your system by executing the following command in your terminal. 

```shell 
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

I also recommend using [Homebrew Cask][homebrew-cask] to install graphical applications like Atom and Google Chrome. 

After you have installed Homebrew, update your package index. 

```shell
brew update
```

Finally, install the following packages required for this course. 

```shell 
brew install apache-arrow
brew install apache-spark
brew install avro-tools
brew install git
brew install hadoop
brew install libtensorflow
brew install pandoc
brew install pandoc-citeproc
brew install pandoc-crossref
brew install parquet-tools
brew install protobuf
brew install snappy
```

Optionally, you can install the following packages using Homebrew Cask. 

```shell
brew cask install anaconda
brew cask install atom
brew cask install github
brew cask install mactex
brew cask install miniconda
brew cask install virtualbox
```

## JDK

Spark and Hadoop use version 8 of the Java Development Kit (JDK 8). [Download the latest version from Oracle][jdk8] and install on your local machine. Once completed, edit your shell profile &ndash; `$HOME/.bash_profile` if you are using Bash or `$HOME/.zshrc` if you are using `Zsh` &ndash; and add the following. 

```
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_211.jdk/Contents/Home
```

## TensorFlow

!!! note
    There is no GPU support for macOS

[homebrew]: https://brew.sh/
[homebrew-cask]: https://github.com/Homebrew/homebrew-cask
[jdk8]: https://www.oracle.com/java/technologies/javase-jdk8-downloads.html
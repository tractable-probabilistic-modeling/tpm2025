# Web pages for the 'UAI 2025 Workshop on Tractable Probabilistic Modeling'

This web page uses Jekyll through GitHub pages for static HTML generation. The website is available under [add url](url). 

## Maintaining / Updating

Content is somewhat decoupled from the HTML/layout and should be edited as follows

* Basic information in `_config.yml` 
* Deadlines (shown on main page and CfP) in `_config.yml` 
* Speaker information in `_data/speakers.yml`
* Speaker photos should go in `assets/speakers/` if available.
* Organizer information in `_data/organizers.yml`
* Navigation menu items (also enable/disable) in `_data/menu.yml`
* Main page content (as HTML) in `index.html`
* Sub-page content (as Markdown) in `_pages/`

## Installation
You will need to install Jekyll on your machine first. See [jekyllrb.com](https://jekyllrb.com/docs/installation/) for detailed guides on installing Ruby, RubyGems and Jekyll on a specific operating system. 

**Note:** I had to do the following additional steps to get Jekyll working:
Install additional packages with the GEM installer: `gem install github-pages`, and `gem install webrick`.

## Previewing / Running locally
After that you can clone this repository, you can run the following:

    jekyll serve --baseurl ""
    
Where the `--baseurl` option overwrites the GitHub-specific path, and makes the page preview available (typically) at http://127.0.0.1:4000/


## Credits
This is adapted based on the workshop website used for the ECCV & ICCV Workshop on Uncertainty Quantification in Computer Vision.

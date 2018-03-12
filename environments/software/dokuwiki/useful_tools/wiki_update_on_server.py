"""
Update wiki data from tar package file.

2016.07.15
"""
import subprocess

WIKI_DATA_PATH = '/work/mywiki/dokuwiki/data'


if __name__ == '__main__':
    my_data = input('Please input your wiki data filename: ')

    test_cmd = [
        'ls -al',
    ]

    print(my_data)
    cmd = [
        'sudo rm -rf media.old2 pages.old2',
        'sudo mv media.old media.old2',
        'sudo mv pages.old pages.old2',
        'sudo mv media media.old',                      # backup
        'sudo mv pages pages.old',                      # backup
        'sudo cp /home/ubuntu/{0} .'.format(my_data),   # update
        'sudo tar xf {0} -C .'.format(my_data),         # update
        'sudo chown -R www-data:www-data pages media',  # reload
        'sudo chmod -R 755 pages media',                # reload
        'sudo rm -rf cache/*',                          # reload
        'sudo service nginx reload',                    # reload
        'sudo rm {0}'.format(my_data)
    ]

    for c in cmd:
        print(c)
        subprocess.run(c.split(), cwd=WIKI_DATA_PATH)

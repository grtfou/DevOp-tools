// Copy remote file (ex. Redis DB-dump.rdb) to local for backup

Date.prototype.ymd = function() {
    var mm = this.getMonth() + 1;
    var dd = this.getDate();

    return [this.getFullYear().toString().substr(2,2),
            (mm>9 ? '' : '0') + mm,
            (dd>9 ? '' : '0') + dd
           ].join('');

};

var exec = require('child_process').exec;
function puts(error, stdout, stderr) { console.log(stdout); }
var date = new Date();
date.ymd();

var cmd = `scp -i <ssh_key> \
           <ssh_account>@<ssh_host>:<remote_file> \
           <local_file>` + date.ymd() + ".<file_extension>";
exec(cmd, puts);

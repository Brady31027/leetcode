use strict;
use warnings;

my $all_files_string = `ls`;
my @all_files = split(/\s+/, $all_files_string);
my @all_py_files = <*.py>;
my @all_folders = ();

sub is_file_existed {
	my $filename = shift;
	for (@all_py_files) {
		my $py = $_;
		if ($py eq $filename){ return 1;}
	}
	return 0;
}


for (@all_files) {
	my $filename = $_;
	if ($filename =~ m/(\d+)_\w+/){
		push @all_folders, $1.'.py';
	}
}
for (@all_folders) {
	my $to_del_file = $_;
	my $confirm_del = is_file_existed($to_del_file);
	if ($confirm_del == 1){
		print "del $to_del_file\n";
		unlink $to_del_file;
	}
}
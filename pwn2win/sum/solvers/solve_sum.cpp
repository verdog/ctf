#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;
typedef unsigned long long int ulli;

static pid_t connect(const char *hostport, FILE* &inf, FILE* &outf) {
	int pipein[2], pipeout[2];
	if (pipe(pipein) != 0 || pipe(pipeout) != 0) {
		perror("pipe");
		exit(1);
	}

	const pid_t pid = fork();
	if (pid == 0) { // Child
		close(pipeout[1]);
		dup2(pipeout[0], STDIN_FILENO);
		close(pipein[0]);
		dup2(pipein[1], STDOUT_FILENO);
		execlp("openssl",
			"openssl", "s_client",
			"-CAfile", "/etc/ssl/certs/ca-certificates.crt",
			"-quiet",
			"-verify", "true",
			"-connect", hostport,
			(const char*)NULL);
		perror("execl");
		exit(1);
	}

	if ((inf = fdopen(pipein[0], "r")) == NULL
			|| (outf = fdopen(pipeout[1], "w")) == NULL) {
		perror("fdopen");
		exit(1);
	}
	setvbuf(inf, NULL, _IONBF, 0);
	setvbuf(outf, NULL, _IONBF, 0);
	return pid;
}

int main() {
	FILE *inf, *outf;
	connect("programming.pwn2.win:9000", inf, outf);

	ulli sum = 0;
	while (true) {
		ulli a;
		if (fscanf(inf, "%llu", &a) != 1) {
			// if unable to read a numeric value, then it's the flag
			char flag[128];
			if(fgets(flag, sizeof(flag), inf) != NULL) {
				printf("flag: %s", flag);
				exit(0);
			}
		}

		if (a == 0) {
			fprintf(outf, "%llu\n", sum);
			printf("sent: %llu\n", sum);  // for debugging purposes
			sum = 0;
		}
		else {
			sum += a;
		}
	}
	return 0;
}

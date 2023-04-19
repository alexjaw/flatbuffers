// refs:
// https://github.com/gaspardpetit/base64
// https://stackoverflow.com/questions/342409/how-do-i-base64-encode-decode-in-c/41094722#41094722
// https://stackoverflow.com/questions/180947/base64-decode-snippet-in-c
#include <iostream>

#include "polfosol.h"
#include "user_generated.h"

using namespace users;

std::string encode(const std::string &bytes) {
	return polfosol::b64encode((unsigned char*)bytes.data(), bytes.length());
}

std::string decode(const std::string &base64) {
	return polfosol::b64decode((unsigned char*)base64.data(), base64.length());
}

int main(int /*argc*/, const char * /*argv*/[]) {
    std::string str = "Hello World";
	std::string encoded = "SGVsbG8gV29ybGQ=";
	//std::cout << str << std::endl;

	std::string encoded_observed = encode(str);
	//std::cout << encoded_observed << std::endl;
	std::string decoded_observed = decode(encoded_observed);
	//std::cout << decoded_observed << std::endl;

	// case user flatbuffer: name: Arthur Dent. id: 42
	encoded = "DAAAAAgAFAAQAAQACAAAACoAAAAAAAAAAAAAAAQAAAALAAAAQXJ0aHVyIERlbnQA";
	std::cout << encoded << std::endl;
	std::string decoded = decode(encoded);
	//std::cout << decoded<< std::endl;

	auto my_user = GetUser((unsigned char*)decoded.data());
	std::cout << my_user->name()->c_str() << std::endl;
	std::cout << my_user->id() << std::endl;
}
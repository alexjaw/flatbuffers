// refs:
// https://github.com/gaspardpetit/base64
// https://stackoverflow.com/questions/342409/how-do-i-base64-encode-decode-in-c/41094722#41094722
// https://stackoverflow.com/questions/180947/base64-decode-snippet-in-c
#include <iostream>

#include "polfosol.h"
#include "classification_generated.h"

using namespace dnn_vision;

std::string encode(const std::string &bytes) {
	return polfosol::b64encode((unsigned char*)bytes.data(), bytes.length());
}

std::string decode(const std::string &base64) {
	return polfosol::b64decode((unsigned char*)base64.data(), base64.length());
}

std::string deserialize(const std::string &base64) {
	std::string r = "TBD";
	std::string decoded = decode(base64);
	//std::cout << decoded<< std::endl;

	auto detections = GetClassificationTop((unsigned char*)decoded.data());
	auto perception = detections->perception();
	auto n = perception->classification_list()->size();
	//std::cout << "n: " << n << std::endl;
	for (int i=0; i<n; ++i) {
		auto class_id = perception->classification_list()->Get(i)->class_id();
		auto score = perception->classification_list()->Get(i)->score();
		std::cout << "i: " << i << ". class_id:" << class_id << ", score:" << score << std::endl;
	}

	return r;
}

void testme() {
	/* Expected output
	i: 0. class_id:593, score:0.121094
    i: 1. class_id:627, score:0.121094
	i: 2. class_id:921, score:0.121094
	i: 3. class_id:95, score:0.0742188
	i: 4. class_id:651, score:0.0585938
    */
	const std::string encoded = "DAAAAAAABgAKAAQABgAAAAwAAAAAAAYACAAEAAYAAAAEAAAABQAAAEwAAAA0AAAAJAAAABQAAAAEAAAA0P///4sCAAAAAHA93P///18AAAAAAJg96P///5kDAAAAAPg99P///3MCAAAAAPg9CAAMAAQACAAIAAAAUQIAAAAA+D0=";
	std::string deserialized = deserialize(encoded);
	std::cout << "deserialized: " << deserialized << std::endl;
}

int main(int /*argc*/, const char * /*argv*/[]) {
	testme();
}
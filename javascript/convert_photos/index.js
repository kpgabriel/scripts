const glob = require('glob');
const sharp = require('sharp');
const fs = require('fs');

// options is optional
glob('D:/Photos/**/*.+(png|jpg|JPG|PNG|jpeg|JPEG)', {}, async (er, files) => {
	// files is an array of filenames.
	// If the `nonull` option is set, and nothing
	// was found, then files is ["**/*.js"]
	// er is an error object or null.
	files.forEach(async (element) => {
		let fileName = element.split('.')[0];
		let newFileName = fileName.replace('Photos', 'PhotosWebp');
		let newFilePath = newFileName
			.split('/')
			.filter((value, idx) => {
				if (idx === newFileName.split('/').length - 1) {
					return '';
				} else {
					return value;
				}
			})
			.join()
			.replace(/,/g, '/');
		// console.log(newFilePath);
		if (fileName.length < 1) {
			console.log('no name');
		}
		// console.log(newFileName)
		try {
			if (!fs.existsSync(`${newFileName}.webp`)) {
				fs.mkdirSync(newFilePath, { recursive: true });
				await sharp(element)
					.withMetadata()
					.toFile(`${newFileName}.webp`);
			}
		} catch (error) {
			console.log(`ERROR!!!!!! on file ${fileName}: `, error);
		}
	});
});

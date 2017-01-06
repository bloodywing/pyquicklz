#define QLZ_VERSION_MAJOR 1
#define QLZ_VERSION_MINOR 5
#define QLZ_VERSION_REVISION 0

typedef unsigned int ui32;
typedef unsigned short int ui16;

size_t qlz_size_decompressed(const char *source);
size_t qlz_size_compressed(const char *source);
size_t qlz_compress(const void *source, char *destination, size_t size, ...);
size_t qlz_decompress(const char *source, void *destination, ...);
int qlz_get_setting(int setting);
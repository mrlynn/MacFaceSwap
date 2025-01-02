'use client';

import React from 'react';
import { ArrowLeft, Clock, Calendar } from 'lucide-react';
import { blogPosts } from '@/lib/blog-data';

export function BlogPost({ slug }) {
  const post = blogPosts[slug];

  if (!post) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-purple-900 to-pink-700 text-white">
        <div className="container mx-auto px-4 py-16 text-center">
          <h1 className="text-4xl font-bold mb-4">Post Not Found</h1>
          <a 
            href="/"
            className="text-pink-300 hover:text-pink-400 inline-flex items-center gap-2"
          >
            <ArrowLeft size={20} />
            Return Home
          </a>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 to-pink-700 text-white">
      <nav className="container mx-auto px-4 py-6">
        <a 
          href="/"
          className="inline-flex items-center gap-2 text-white hover:text-pink-300"
        >
          <ArrowLeft size={20} />
          Back to Home
        </a>
      </nav>

      {/* Full-width header image container */}
      <div className="w-full h-[400px] relative mb-12">
        <img
          src={post.headerImage.src}
          alt={post.headerImage.alt}
          className="w-full h-full object-cover"
        />
        {/* Gradient overlay */}
        <div className="absolute inset-0 bg-gradient-to-t from-purple-900 via-purple-900/50 to-transparent"></div>
        
        {/* Header content positioned over the image */}
        <div className="absolute bottom-0 left-0 right-0 container mx-auto px-4 py-12">
          <div className="flex items-center gap-4 mb-4">
            <span className="bg-pink-500 text-white px-3 py-1 rounded-full text-sm">
              {post.category}
            </span>
            <div className="flex items-center gap-4 text-pink-100">
              <span className="flex items-center gap-1">
                <Calendar size={16} />
                {post.date}
              </span>
              <span className="flex items-center gap-1">
                <Clock size={16} />
                {post.readTime}
              </span>
            </div>
          </div>
          <h1 className="text-4xl font-bold text-white mb-4">{post.title}</h1>
          <p className="text-xl text-pink-100 max-w-2xl">{post.excerpt}</p>
        </div>
      </div>

      <article className="container mx-auto px-4 py-12 max-w-4xl">
        <div 
          className="prose prose-invert prose-pink max-w-none"
          dangerouslySetInnerHTML={{ __html: post.content }}
        />
      </article>
    </div>
  );
}